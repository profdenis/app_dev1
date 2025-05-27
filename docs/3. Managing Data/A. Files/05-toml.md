# Working with TOML Configuration Files

## What is TOML?

TOML (Tom's Obvious, Minimal Language) is a configuration file format designed to be easy to read and write due to its
obvious semantics. It was created by Tom Preston-Werner, the co-founder of GitHub, as a more human-friendly alternative
to other configuration formats.

### Key Features of TOML

- **Human-readable**: Clean, intuitive syntax that's easy to understand
- **Unambiguous**: Clear semantics with no surprising edge cases
- **Minimal**: Simple syntax without unnecessary complexity
- **Type-aware**: Native support for strings, integers, floats, booleans, dates, arrays, and tables

### TOML vs Other Formats

| Feature        | TOML        | JSON      | YAML      | INI       |
|----------------|-------------|-----------|-----------|-----------|
| Human-readable | ✅ Excellent | ❌ Verbose | ✅ Good    | ✅ Good    |
| Comments       | ✅ Yes       | ❌ No      | ✅ Yes     | ✅ Yes     |
| Data types     | ✅ Rich      | ✅ Good    | ✅ Rich    | ❌ Limited |
| Hierarchical   | ✅ Yes       | ✅ Yes     | ✅ Yes     | ❌ Limited |
| Complexity     | ✅ Simple    | ✅ Simple  | ❌ Complex | ✅ Simple  |

## Where TOML is Used

TOML has become popular in the Python ecosystem and beyond:

### Python Projects

- **Poetry** (`pyproject.toml`) - Python dependency management
- **Black** - Code formatter configuration
- **pytest** - Testing framework configuration
- **setuptools** - Package building configuration
- **pip** - Package installer configuration

### Other Languages and Tools

- **Rust** (`Cargo.toml`) - Package manager configuration
- **Hugo** - Static site generator configuration
- **Netlify** - Deployment configuration
- **Docker Compose** - Alternative to YAML format

### Why TOML for Configuration?

1. **Readable**: Non-technical users can understand and modify settings
2. **Comments**: Document why certain settings exist
3. **Type safety**: Reduces configuration errors
4. **Validation**: Easy to validate structure and types
5. **Version control friendly**: Clear diffs when settings change

## Installing the TOML Library

Python 3.11+ includes `tomllib` in the standard library (read-only). For older versions or write support, install a
third-party library:

```bash
# For Python 3.11+, tomllib is built-in (read-only)
# For writing or older Python versions:
pip install toml
# or
pip install tomli tomli-w  # Faster alternatives
```

## Basic TOML Operations

### Basic TOML Syntax

```toml
# This is a comment in TOML

# Basic key-value pairs
title = "My Application"
version = "1.0.0"
debug = true
max_connections = 100
timeout = 30.5

# Arrays
allowed_hosts = ["localhost", "127.0.0.1", "example.com"]
ports = [8000, 8001, 8002]

# Tables (similar to dictionaries/objects)
[database]
host = "localhost"
port = 5432
name = "myapp"
username = "admin"

# Nested tables
[database.pool]
min_size = 5
max_size = 20

# Array of tables
[[servers]]
name = "web1"
ip = "192.168.1.10"

[[servers]]
name = "web2"
ip = "192.168.1.11"
```

### Reading TOML Files

```python
# For Python 3.11+
import tomllib


# For older Python versions or third-party libraries
# import toml

def read_config(filename):
    """Read TOML configuration file"""
    try:
        # Python 3.11+ approach
        with open(filename, 'rb') as file:
            config = tomllib.load(file)

        # Alternative for older Python versions:
        # with open(filename, 'r', encoding='utf-8') as file:
        #     config = toml.load(file)

        return config

    except FileNotFoundError:
        print(f"Configuration file {filename} not found")
        return {}
    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML file: {e}")
        return {}


# Usage
config = read_config('config.toml')
print(f"App title: {config.get('title', 'Unknown')}")
print(f"Database host: {config.get('database', {}).get('host', 'localhost')}")
```

### Writing TOML Files

```python
import toml  # Third-party library required for writing


def write_config(filename, config_data):
    """Write configuration to TOML file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            toml.dump(config_data, file)
        print(f"Configuration saved to {filename}")
        return True

    except Exception as e:
        print(f"Error writing configuration: {e}")
        return False


# Sample configuration data
config = {
    'title': 'My Application',
    'version': '1.0.0',
    'debug': True,
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'myapp'
    },
    'allowed_hosts': ['localhost', '127.0.0.1']
}

# Write configuration
write_config('output.toml', config)
```

## Comprehensive Application Configuration Example

### Sample Configuration File (`app_config.toml`)

```toml
# Application Configuration File
# Generated automatically - modify with care

[app]
name = "WebAPI Server"
version = "2.1.0"
description = "A high-performance web API server"
debug = false
environment = "production"

# Server configuration
[server]
host = "0.0.0.0"
port = 8000
workers = 4
timeout = 30
max_request_size = "10MB"
allowed_methods = ["GET", "POST", "PUT", "DELETE"]

# Database configuration
[database]
engine = "postgresql"
host = "db.example.com"
port = 5432
name = "webapp_prod"
username = "webapp_user"
# Note: Password should be in environment variables, not config files
max_connections = 20
timeout = 30.0
ssl_required = true

# Connection pool settings
[database.pool]
min_size = 5
max_size = 20
acquire_timeout = 10.0
recycle_time = 3600

# Redis cache configuration
[cache]
enabled = true
backend = "redis"
host = "cache.example.com"
port = 6379
database = 0
key_prefix = "webapp:"
default_timeout = 300

# Logging configuration
[logging]
level = "INFO"
format = "{time} | {level} | {name} | {message}"
file_enabled = true
file_path = "/var/log/webapp/app.log"
file_rotation = "daily"
file_retention = 30

# Console logging
[logging.console]
enabled = true
colored = true

# Email notifications
[email]
enabled = true
smtp_host = "smtp.example.com"
smtp_port = 587
use_tls = true
from_address = "noreply@example.com"
admin_emails = ["admin@example.com", "ops@example.com"]

# Security settings
[security]
secret_key_env = "APP_SECRET_KEY"  # Environment variable name
jwt_expiry_hours = 24
bcrypt_rounds = 12
rate_limit_per_minute = 60
cors_origins = ["https://app.example.com", "https://admin.example.com"]

# Feature flags
[features]
user_registration = true
email_verification = true
two_factor_auth = false
admin_dashboard = true
api_analytics = true

# External API integrations
[[integrations]]
name = "payment_gateway"
enabled = true
base_url = "https://api.payments.com"
timeout = 15
retry_attempts = 3

[[integrations]]
name = "email_service"
enabled = true
base_url = "https://api.emailprovider.com"
timeout = 10
retry_attempts = 2

# Monitoring and metrics
[monitoring]
enabled = true
metrics_port = 9090
health_check_path = "/health"
metrics_path = "/metrics"

[monitoring.alerts]
cpu_threshold = 80.0
memory_threshold = 85.0
disk_threshold = 90.0
response_time_threshold = 1000  # milliseconds
```

### Configuration Manager Class

```python
import tomllib
import toml
from pathlib import Path
from typing import Dict, Any, Optional
import os


class ConfigurationManager:
    """Manages application configuration using TOML files"""

    def __init__(self, config_file: str = "config.toml"):
        self.config_file = Path(config_file)
        self.config = {}
        self._load_config()

    def _load_config(self):
        """Load configuration from TOML file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'rb') as file:
                    self.config = tomllib.load(file)
                print(f"Configuration loaded from {self.config_file}")
            else:
                print(f"Configuration file {self.config_file} not found, using defaults")
                self._create_default_config()

        except tomllib.TOMLDecodeError as e:
            print(f"Error parsing TOML configuration: {e}")
            print("Using default configuration")
            self._create_default_config()

    def _create_default_config(self):
        """Create default configuration"""
        self.config = {
            'app': {
                'name': 'My Application',
                'version': '1.0.0',
                'debug': True,
                'environment': 'development'
            },
            'server': {
                'host': 'localhost',
                'port': 8000,
                'workers': 1
            },
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp_dev',
                'max_connections': 10
            },
            'logging': {
                'level': 'DEBUG',
                'console': {'enabled': True}
            }
        }

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation
        Example: get('database.host') or get('server.port')
        """
        keys = key_path.split('.')
        value = self.config

        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

    def set(self, key_path: str, value: Any):
        """
        Set configuration value using dot notation
        Example: set('database.host', 'new-host')
        """
        keys = key_path.split('.')
        config_section = self.config

        # Navigate to the parent section
        for key in keys[:-1]:
            if key not in config_section:
                config_section[key] = {}
            config_section = config_section[key]

        # Set the final value
        config_section[keys[-1]] = value

    def save(self, filename: Optional[str] = None):
        """Save current configuration to TOML file"""
        target_file = Path(filename) if filename else self.config_file

        try:
            with open(target_file, 'w', encoding='utf-8') as file:
                toml.dump(self.config, file)
            print(f"Configuration saved to {target_file}")
            return True
        except Exception as e:
            print(f"Error saving configuration: {e}")
            return False

    def validate(self) -> bool:
        """Validate configuration for required fields"""
        required_sections = ['app', 'server', 'database']
        errors = []

        for section in required_sections:
            if section not in self.config:
                errors.append(f"Missing required section: [{section}]")

        # Validate specific required fields
        required_fields = {
            'app.name': str,
            'app.version': str,
            'server.host': str,
            'server.port': int,
            'database.host': str,
            'database.port': int
        }

        for field_path, expected_type in required_fields.items():
            value = self.get(field_path)
            if value is None:
                errors.append(f"Missing required field: {field_path}")
            elif not isinstance(value, expected_type):
                errors.append(f"Field {field_path} must be of type {expected_type.__name__}")

        if errors:
            print("Configuration validation errors:")
            for error in errors:
                print(f"  - {error}")
            return False

        print("Configuration validation passed")
        return True

    def get_database_url(self) -> str:
        """Generate database URL from configuration"""
        db_config = self.config.get('database', {})
        username = db_config.get('username', '')
        password = os.getenv('DB_PASSWORD', '')  # Get from environment
        host = db_config.get('host', 'localhost')
        port = db_config.get('port', 5432)
        name = db_config.get('name', 'myapp')

        if username and password:
            return f"postgresql://{username}:{password}@{host}:{port}/{name}"
        else:
            return f"postgresql://{host}:{port}/{name}"

    def is_development(self) -> bool:
        """Check if running in development environment"""
        return self.get('app.environment', 'development') == 'development'

    def is_debug_enabled(self) -> bool:
        """Check if debug mode is enabled"""
        return self.get('app.debug', False)

    def get_server_address(self) -> tuple:
        """Get server host and port as tuple"""
        host = self.get('server.host', 'localhost')
        port = self.get('server.port', 8000)
        return (host, port)

    def print_summary(self):
        """Print configuration summary"""
        print(f"\n=== Configuration Summary ===")
        print(f"App: {self.get('app.name')} v{self.get('app.version')}")
        print(f"Environment: {self.get('app.environment')}")
        print(f"Debug: {self.get('app.debug')}")
        print(f"Server: {self.get('server.host')}:{self.get('server.port')}")
        print(f"Database: {self.get('database.host')}:{self.get('database.port')}")
        print(f"Log Level: {self.get('logging.level')}")

        if self.get('features'):
            enabled_features = [k for k, v in self.get('features', {}).items() if v]
            print(f"Features: {', '.join(enabled_features)}")

        print("=" * 30)


# Example usage and testing
def main():
    """Example usage of ConfigurationManager"""

    # Initialize configuration manager
    config = ConfigurationManager('app_config.toml')

    # Validate configuration
    if not config.validate():
        print("Configuration validation failed!")
        return

    # Print configuration summary
    config.print_summary()

    # Access configuration values
    print(f"\nAccessing configuration:")
    print(f"App name: {config.get('app.name')}")
    print(f"Server port: {config.get('server.port')}")
    print(f"Database host: {config.get('database.host')}")
    print(f"Debug enabled: {config.is_debug_enabled()}")
    print(f"Development mode: {config.is_development()}")

    # Get database URL
    print(f"Database URL: {config.get_database_url()}")

    # Access nested configuration
    log_level = config.get('logging.level', 'INFO')
    console_enabled = config.get('logging.console.enabled', True)
    print(f"Logging: {log_level}, Console: {console_enabled}")

    # Access array configurations
    allowed_methods = config.get('server.allowed_methods', [])
    print(f"Allowed HTTP methods: {allowed_methods}")

    # Access array of tables
    integrations = config.get('integrations', [])
    enabled_integrations = [i['name'] for i in integrations if i.get('enabled')]
    print(f"Enabled integrations: {enabled_integrations}")

    # Demonstrate configuration modification
    print(f"\nModifying configuration:")
    config.set('app.debug', False)
    config.set('server.port', 9000)
    print(f"Debug now: {config.get('app.debug')}")
    print(f"Port now: {config.get('server.port')}")

    # Save modified configuration
    config.save('modified_config.toml')


if __name__ == "__main__":
    main()
```

### Environment-Specific Configuration

```python
import os
from pathlib import Path


class EnvironmentConfigManager(ConfigurationManager):
    """Configuration manager with environment-specific overrides"""

    def __init__(self, base_config: str = "config.toml"):
        self.environment = os.getenv('APP_ENV', 'development')
        self.base_config_file = Path(base_config)

        # Load base configuration first
        super().__init__(base_config)

        # Then load environment-specific overrides
        self._load_environment_config()

    def _load_environment_config(self):
        """Load environment-specific configuration overrides"""
        env_config_file = self.base_config_file.parent / f"config.{self.environment}.toml"

        if env_config_file.exists():
            try:
                with open(env_config_file, 'rb') as file:
                    env_config = tomllib.load(file)

                # Merge environment config with base config
                self._deep_merge(self.config, env_config)
                print(f"Environment configuration loaded from {env_config_file}")

            except tomllib.TOMLDecodeError as e:
                print(f"Error parsing environment configuration: {e}")

    def _deep_merge(self, base_dict: dict, override_dict: dict):
        """Deep merge two dictionaries"""
        for key, value in override_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._deep_merge(base_dict[key], value)
            else:
                base_dict[key] = value


# Usage example
def create_environment_configs():
    """Create sample environment-specific configuration files"""

    # Development overrides
    dev_config = {
        'app': {
            'debug': True,
            'environment': 'development'
        },
        'server': {
            'host': 'localhost',
            'port': 8000,
            'workers': 1
        },
        'database': {
            'host': 'localhost',
            'name': 'myapp_dev'
        },
        'logging': {
            'level': 'DEBUG'
        }
    }

    # Production overrides
    prod_config = {
        'app': {
            'debug': False,
            'environment': 'production'
        },
        'server': {
            'host': '0.0.0.0',
            'port': 80,
            'workers': 4
        },
        'database': {
            'host': 'prod-db.example.com',
            'name': 'myapp_prod'
        },
        'logging': {
            'level': 'INFO'
        }
    }

    # Save environment-specific configs
    with open('config.development.toml', 'w') as f:
        toml.dump(dev_config, f)

    with open('config.production.toml', 'w') as f:
        toml.dump(prod_config, f)

    print("Environment-specific configuration files created")


# Example usage
if __name__ == "__main__":
    # Set environment (normally done via environment variable)
    os.environ['APP_ENV'] = 'development'

    # Create sample environment configs
    create_environment_configs()

    # Use environment-aware configuration
    config = EnvironmentConfigManager('app_config.toml')
    config.print_summary()
```

## Best Practices for TOML Configuration

### 1. Structure and Organization

- Group related settings into tables
- Use clear, descriptive key names
- Keep nesting to a reasonable depth (2-3 levels max)
- Use consistent naming conventions (snake_case recommended)

### 2. Security Considerations

```toml
# Good: Reference environment variables for secrets
[database]
password_env = "DB_PASSWORD"  # Environment variable name

# Bad: Never store secrets in config files
# password = "super_secret_password"  # DON'T DO THIS

[security]
secret_key_env = "APP_SECRET_KEY"
jwt_secret_env = "JWT_SECRET"
```

### 3. Documentation and Comments

```toml
# Application Configuration
# Last updated: 2024-01-15
# Environment: Production

[server]
# Maximum number of worker processes
# Recommended: 2 * CPU cores
workers = 4

# Request timeout in seconds
# Increase for slow endpoints
timeout = 30
```

### 4. Validation and Error Handling

Always validate your configuration:

```python
def validate_config_types(config):
    """Validate configuration data types"""
    type_checks = [
        ('server.port', int, lambda x: 1 <= x <= 65535),
        ('server.workers', int, lambda x: x > 0),
        ('database.max_connections', int, lambda x: x > 0),
        ('app.debug', bool, None),
    ]

    for path, expected_type, validator in type_checks:
        value = config.get(path)
        if value is not None:
            if not isinstance(value, expected_type):
                raise ValueError(f"{path} must be {expected_type.__name__}")
            if validator and not validator(value):
                raise ValueError(f"{path} failed validation")
```

## Key Points to Remember

1. **TOML is for configuration**: Perfect for app settings, not general data storage
2. **Human-readable**: Designed to be edited by humans
3. **Type-aware**: Supports rich data types natively
4. **Comments matter**: Document your configuration choices
5. **Environment separation**: Use different files for different environments
6. **Security first**: Never store secrets in configuration files
7. **Validation**: Always validate configuration after loading
8. **Default values**: Provide sensible defaults for optional settings

## Common Mistakes to Avoid

- Storing passwords or API keys in TOML files
- Creating overly complex nested structures
- Not validating configuration data
- Mixing configuration with runtime data
- Not using environment-specific configurations
- Forgetting to handle missing configuration files
- Not documenting configuration options

TOML provides an excellent balance of simplicity and power for application configuration, making it easy for both
developers and operators to understand and modify application settings.


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.