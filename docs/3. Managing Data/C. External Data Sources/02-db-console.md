# DB interaction - Console Example

```python
import getpass

import psycopg2
from psycopg2 import Error
from contextlib import contextmanager


class DatabaseConnection:
    def __init__(self, host, database, user, password, port=5432, schema='public'):
        self.connection_params = {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'port': port,
            'options': f'-c search_path={schema}'
        }

    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        connection = None
        try:
            connection = psycopg2.connect(**self.connection_params)
            yield connection
        except Error as e:
            if connection:
                connection.rollback()
            raise e
        finally:
            if connection:
                connection.close()

    def execute_query(self, query, params=None):
        """Execute a SELECT query and return results"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_update(self, query, params=None):
        """Execute INSERT, UPDATE, or DELETE query"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount


class NorthwindDatabase:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_categories(self):
        """Get all product categories"""
        query = "SELECT category_id, category_name FROM categories ORDER BY category_name"
        return self.db.execute_query(query)

    def get_products_by_category(self, category_id):
        """Get products for a specific category"""
        query = """
                SELECT product_id, product_name, unit_price, units_in_stock
                FROM products
                WHERE category_id = %s
                ORDER BY product_name \
                """
        return self.db.execute_query(query, (category_id,))

    def get_product_details(self, product_id):
        """Get detailed information about a product"""
        query = """
                SELECT p.product_name, \
                       p.unit_price, \
                       p.units_in_stock,
                       c.category_name, \
                       s.company_name as supplier
                FROM products p
                         JOIN categories c ON p.category_id = c.category_id
                         JOIN suppliers s ON p.supplier_id = s.supplier_id
                WHERE p.product_id = %s \
                """
        result = self.db.execute_query(query, (product_id,))
        return result[0] if result else None


def main():
    user = input("Enter your database username: ")
    password = getpass.getpass("Enter your database password: ")
    # Initialize database connection
    db_conn = DatabaseConnection(
        host='localhost',
        database='denis',
        user=user,
        password=password,
        schema='northwind'
    )

    # Initialize data access layer
    northwind = NorthwindDatabase(db_conn)

    try:
        print("Northwind Product Catalog")
        print("-" * 30)

        # Display categories
        categories = northwind.get_categories()
        print("\nAvailable Categories:")
        for cat_id, cat_name in categories:
            print(f"{cat_id}: {cat_name}")

        # Get user selection
        selected_cat = input("\nEnter category ID: ")

        # Display products in selected category
        products = northwind.get_products_by_category(int(selected_cat))
        print(f"\nProducts in selected category:")

        for prod_id, name, price, stock in products:
            print(f"{prod_id}: {name} - ${price:.2f} ({stock} in stock)")

    except Exception as e:
        print(f"Application error: {e}")


if __name__ == "__main__":
    main()
```


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.