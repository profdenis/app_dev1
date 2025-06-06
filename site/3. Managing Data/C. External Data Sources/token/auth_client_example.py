#!/usr/bin/env python3
"""
REST API Authentication Client Example

This demonstrates how to authenticate with a REST API and use tokens
to access protected endpoints.

Prerequisites:
1. Run the FastAPI server (auth_server_fastapi.py) first
2. pip install requests

This example shows:
- How to login and get an authentication token
- How to use the token in API requests
- How to handle authentication errors
- How to manage token lifecycle (store, use, clear)

Test credentials for the server:
- username: student, password: password123
- username: teacher, password: secret456
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


class ApiClient:
    """
    API client with token-based authentication
    
    This class demonstrates the complete authentication flow:
    1. Login with credentials to get token
    2. Store token for future requests
    3. Include token in Authorization header
    4. Handle authentication errors
    5. Clear token on logout
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.token = None
        self.token_type = "bearer"
        self.token_expires_at = None
        self.username = None
        
        # Create a session for connection reuse
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
    
    def login(self, username: str, password: str) -> bool:
        """
        Authenticate with the API and store the received token
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            bool: True if login successful, False otherwise
        """
        print(f"🔐 Attempting to login as '{username}'...")
        
        # Prepare login data
        login_data = {
            "username": username,
            "password": password
        }
        
        try:
            # Make login request
            response = self.session.post(
                f"{self.base_url}/login",
                json=login_data,
                timeout=10
            )
            
            if response.status_code == 200:
                # Parse the token response
                token_data = response.json()
                
                # Store authentication data
                self.token = token_data["access_token"]
                self.token_type = token_data["token_type"]
                self.username = username
                
                # Calculate expiration time
                expires_in_seconds = token_data.get("expires_in", 1800)  # Default 30 min
                self.token_expires_at = datetime.now() + timedelta(seconds=expires_in_seconds)
                
                # Update session headers to include token
                self.session.headers.update({
                    "Authorization": f"{self.token_type} {self.token}"
                })
                
                print(f"✅ Login successful!")
                print(f"   Token type: {self.token_type}")
                print(f"   Token expires at: {self.token_expires_at.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   Token (first 30 chars): {self.token[:30]}...")
                
                return True
                
            elif response.status_code == 401:
                print("❌ Login failed: Invalid username or password")
                return False
            else:
                print(f"❌ Login failed: HTTP {response.status_code}")
                print(f"   Response: {response.text}")
                return False
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection error: Is the API server running on http://localhost:8000?")
            return False
        except requests.exceptions.Timeout:
            print("❌ Request timeout: Server took too long to respond")
            return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return False
        except json.JSONDecodeError:
            print("❌ Invalid response format from server")
            return False
    
    def is_authenticated(self) -> bool:
        """Check if we have a valid token that hasn't expired"""
        if not self.token:
            return False
        
        if self.token_expires_at and datetime.now() >= self.token_expires_at:
            print("⚠️  Token has expired")
            return False
        
        return True
    
    def logout(self):
        """Clear stored authentication data"""
        print("🚪 Logging out...")
        self.token = None
        self.token_type = "bearer"
        self.token_expires_at = None
        self.username = None
        
        # Remove Authorization header from session
        if "Authorization" in self.session.headers:
            del self.session.headers["Authorization"]
        
        print("✅ Logged out successfully")
    
    def get_protected_data(self) -> Optional[Dict[str, Any]]:
        """Access a protected endpoint that requires authentication"""
        if not self.is_authenticated():
            print("❌ Not authenticated. Please login first.")
            return None
        
        print("🌐 Accessing protected endpoint...")
        
        try:
            response = self.session.get(f"{self.base_url}/protected", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Protected endpoint accessed successfully!")
                print(f"   Message: {data['message']}")
                return data
                
            elif response.status_code == 401:
                print("❌ Authentication failed: Token invalid or expired")
                self.logout()  # Clear invalid token
                return None
            else:
                print(f"❌ Request failed: HTTP {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def get_user_info(self) -> Optional[Dict[str, Any]]:
        """Get current user information"""
        if not self.is_authenticated():
            print("❌ Not authenticated. Please login first.")
            return None
        
        print("👤 Getting user information...")
        
        try:
            response = self.session.get(f"{self.base_url}/users/me", timeout=10)
            
            if response.status_code == 200:
                user_data = response.json()
                print("✅ User information retrieved!")
                print(f"   Name: {user_data['full_name']}")
                print(f"   Email: {user_data['email']}")
                print(f"   Username: {user_data['username']}")
                return user_data
            elif response.status_code == 401:
                print("❌ Authentication failed: Token invalid or expired")
                self.logout()
                return None
            else:
                print(f"❌ Request failed: HTTP {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def get_posts(self) -> Optional[list]:
        """Get all posts - requires authentication"""
        if not self.is_authenticated():
            print("❌ Not authenticated. Please login first.")
            return None
        
        print("📝 Getting posts...")
        
        try:
            response = self.session.get(f"{self.base_url}/posts", timeout=10)
            
            if response.status_code == 200:
                posts = response.json()
                print(f"✅ Retrieved {len(posts)} posts!")
                
                for post in posts:
                    print(f"   📄 {post['title']} (by {post['author']})")
                
                return posts
            elif response.status_code == 401:
                print("❌ Authentication failed: Token invalid or expired")
                self.logout()
                return None
            else:
                print(f"❌ Request failed: HTTP {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def create_post(self, title: str, content: str) -> Optional[Dict[str, Any]]:
        """Create a new post - requires authentication"""
        if not self.is_authenticated():
            print("❌ Not authenticated. Please login first.")
            return None
        
        print(f"✏️  Creating new post: '{title}'...")
        
        post_data = {
            "title": title,
            "content": content
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/posts",
                json=post_data,
                timeout=10
            )
            
            if response.status_code == 200:
                new_post = response.json()
                print("✅ Post created successfully!")
                print(f"   ID: {new_post['id']}")
                print(f"   Title: {new_post['title']}")
                print(f"   Author: {new_post['author']}")
                return new_post
            elif response.status_code == 401:
                print("❌ Authentication failed: Token invalid or expired")
                self.logout()
                return None
            else:
                print(f"❌ Request failed: HTTP {response.status_code}")
                print(f"   Response: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None


def demonstrate_authentication_flow():
    """Demonstrate the complete authentication flow"""
    print("=" * 60)
    print("🎓 REST API Authentication Demo")
    print("=" * 60)
    print("Make sure the FastAPI server is running on http://localhost:8000")
    print("You can start it with: python auth_server_fastapi.py")
    print()
    
    # Create API client
    client = ApiClient()
    
    print("📚 STEP 1: Test server connection")
    print("-" * 30)
    try:
        response = requests.get("http://localhost:8000/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
        else:
            print("❌ Server responded with error")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on http://localhost:8000")
        return
    
    print("\n📚 STEP 2: Attempt login with valid credentials")
    print("-" * 30)
    success = client.login("student", "password123")
    
    if success:
        print("\n📚 STEP 3: Access protected endpoints")
        print("-" * 30)
        
        # Test protected endpoint
        client.get_protected_data()
        
        print()
        # Get user info
        client.get_user_info()
        
        print()
        # Get posts
        client.get_posts()
        
        print()
        # Create a new post
        client.create_post(
            "My API Test Post",
            "This post was created using the Python API client!"
        )
        
        print("\n📚 STEP 4: Test authentication errors")
        print("-" * 30)
        
        # Manually invalidate token to test error handling
        original_token = client.token
        client.token = "invalid_token_for_testing"
        client.session.headers["Authorization"] = "bearer invalid_token_for_testing"
        
        print("🧪 Testing with invalid token...")
        client.get_protected_data()
        
        # Restore valid token
        client.token = original_token
        client.session.headers["Authorization"] = f"bearer {original_token}"
        print("🔄 Restored valid token")
        
        print("\n📚 STEP 5: Logout")
        print("-" * 30)
        client.logout()
        
        print("\n📚 STEP 6: Try to access protected endpoint after logout")
        print("-" * 30)
        client.get_protected_data()
    
    print("\n📚 STEP 7: Test invalid login")
    print("-" * 30)
    client.login("student", "wrong_password")


def demonstrate_manual_token_usage():
    """Show how to manually handle tokens in requests"""
    print("\n" + "=" * 60)
    print("🔧 Manual Token Usage Examples")
    print("=" * 60)
    
    # First, get a token
    login_data = {"username": "student", "password": "password123"}
    
    try:
        print("1️⃣  Getting token manually...")
        response = requests.post("http://localhost:8000/login", json=login_data)
        
        if response.status_code == 200:
            token_data = response.json()
            token = token_data["access_token"]
            print(f"✅ Token received: {token[:30]}...")
            
            print("\n2️⃣  Using token in manual requests...")
            
            # Method 1: Add token to each request manually
            headers = {"Authorization": f"bearer {token}"}
            response = requests.get("http://localhost:8000/protected", headers=headers)
            
            if response.status_code == 200:
                print("✅ Manual request successful!")
                data = response.json()
                print(f"   Response: {data['message']}")
            
            # Method 2: Using requests.Session
            print("\n3️⃣  Using session with token...")
            session = requests.Session()
            session.headers.update({"Authorization": f"bearer {token}"})
            
            response = session.get("http://localhost:8000/users/me")
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Session request successful!")
                print(f"   User: {user_data['full_name']}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Server not running")


def show_key_concepts():
    """Show important concepts for students"""
    print("\n" + "=" * 60)
    print("🎯 Key Concepts for Students")
    print("=" * 60)
    
    print("""
🔹 Authentication Flow:
   1. POST credentials to /login endpoint
   2. Receive token in response
   3. Include token in Authorization header for protected requests
   4. Handle 401 errors (invalid/expired tokens)

🔹 Token Storage:
   ✅ Store in memory (for desktop apps)
   ✅ Store in secure storage (mobile apps)
   ❌ Never store in plain text files
   ❌ Never hardcode in source code

🔹 HTTP Headers:
   Authorization: bearer your_jwt_token_here
   Content-Type: application/json

🔹 Common Status Codes:
   200 - OK (success)
   201 - Created (successful POST)
   401 - Unauthorized (bad/expired token)
   403 - Forbidden (valid token, insufficient permissions)

🔹 Best Practices:
   • Use requests.Session() for multiple requests
   • Handle token expiration gracefully
   • Clear tokens on logout
   • Use HTTPS in production
   • Implement token refresh if needed
""")


def main():
    """Run all demonstrations"""
    demonstrate_authentication_flow()
    demonstrate_manual_token_usage()
    show_key_concepts()
    
    print("\n" + "=" * 60)
    print("✅ Authentication Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
