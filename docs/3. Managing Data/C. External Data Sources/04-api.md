# Getting Data from REST APIs

## What is a REST API?

A REST API (Representational State Transfer Application Programming Interface) is a way for different software
applications to communicate with each other over the internet. Think of it as a waiter in a restaurant - you make a
request (order), and the API brings back the data (your meal).

## Prerequisites

Before we start, you need to install the `requests` library, which makes working with APIs much easier:

```bash
pip install requests
```

## Basic API Request - Example 1: Getting a Single Post

Let's start with the simplest possible example. We'll use JSONPlaceholder, a free fake REST API for testing and
prototyping.

```python
import requests

# Step 1: Define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Step 2: Make the GET request
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the JSON response
    data = response.json()

    # Step 5: Display the results
    print("API call successful!")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
    print(f"User ID: {data['userId']}")
    print(f"Post ID: {data['id']}")
else:
    print(f"Error: {response.status_code}")
```

### What's happening here?

1. **Import requests**: This library handles all the complex HTTP communication
2. **Define URL**: The endpoint we want to get data from
3. **Make request**: `requests.get()` sends a GET request to the server
4. **Check status**: Status code 200 means "OK" - the request succeeded
5. **Parse JSON**: `.json()` converts the response into a Python dictionary
6. **Display data**: Access the data using dictionary keys

## Example 2: Getting Multiple Items

Now let's get a list of multiple posts:

```python
import requests

# Get multiple posts
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    print(f"Retrieved {len(posts)} posts")
    print("\nFirst 5 posts:")
    print("-" * 50)

    # Display first 5 posts
    for post in posts[:5]:
        print(f"Post {post['id']}: {post['title']}")
        print(f"   Body: {post['body'][:50]}...")  # First 50 characters
        print()
else:
    print(f"Error: {response.status_code}")
```

## Example 3: Adding Error Handling

Here's a more robust version with proper error handling:

```python
import requests


def get_user_info(user_id):
    """Get information about a specific user"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        # Make the request with a timeout
        response = requests.get(url, timeout=5)

        # Check if request was successful
        if response.status_code == 200:
            user = response.json()

            print("User Information:")
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print(f"Company: {user['company']['name']}")

        elif response.status_code == 404:
            print("User not found!")
        else:
            print(f"API error: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Request timed out - server might be slow")
    except requests.exceptions.ConnectionError:
        print("Connection error - check your internet connection")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Test the function
get_user_info(1)
print("\n" + "=" * 50 + "\n")
get_user_info(999)  # This will return 404 - not found
```

## Key Concepts to Remember

### HTTP Status Codes

- **200**: Success - everything worked
- **404**: Not Found - the resource doesn't exist
- **500**: Server Error - something went wrong on the server
- **403**: Forbidden - you don't have permission

### Common Request Methods

- **GET**: Retrieve data (what we're using here)
- **POST**: Send new data to create something
- **PUT**: Update existing data
- **DELETE**: Remove data

### JSON Data Format

APIs typically return data in JSON format, which Python can easily convert to dictionaries and lists:

```python
# JSON response looks like this:
{
    "id": 1,
    "title": "My Post",
    "userId": 1
}

# Python converts it to:
data = {
    "id": 1,
    "title": "My Post",
    "userId": 1
}

# Access with: data["title"]
```

## Practice Exercises

Try these exercises to practice:

1. **Get all users** and display just their names and email addresses
2. **Get all posts by user 1** (hint: use `/posts?userId=1`)
3. **Add error handling** to gracefully handle network problems

## Sending Data to APIs - POST Requests

Now that you know how to GET data from APIs, let's learn how to SEND data to APIs using POST requests.

### Example 4: Creating a New Post

```python
import requests
import json


def create_new_post():
    """Send data to API to create a new post"""
    url = "https://jsonplaceholder.typicode.com/posts"

    # Step 1: Prepare the data to send
    new_post = {
        "title": "My First API Post",
        "body": "This is the content of my post created via API",
        "userId": 1
    }

    # Step 2: Set headers to tell the server we're sending JSON
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Step 3: Make the POST request
        response = requests.post(url, json=new_post, headers=headers)

        # Step 4: Check if the request was successful
        if response.status_code == 201:  # 201 = Created successfully
            created_post = response.json()

            print("Post created successfully!")
            print(f"New post ID: {created_post['id']}")
            print(f"Title: {created_post['title']}")
            print(f"Body: {created_post['body']}")
            print(f"User ID: {created_post['userId']}")

        else:
            print(f"Error creating post: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


# Test the function
create_new_post()
```

### Example 5: Interactive Post Creation

Let's make it interactive so users can input their own data:

```python
import requests


def create_post_interactive():
    """Let user input data and create a post"""
    print("Create a New Post")
    print("-" * 20)

    # Get user input
    title = input("Enter post title: ")
    body = input("Enter post content: ")
    user_id = input("Enter your user ID (1-10): ")

    # Validate user_id is a number
    try:
        user_id = int(user_id)
    except ValueError:
        print("Invalid user ID. Using default (1)")
        user_id = 1

    # Prepare data
    post_data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    # API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send POST request
        response = requests.post(url, json=post_data)

        if response.status_code == 201:
            result = response.json()
            print("\n✅ Post created successfully!")
            print(f"Post ID: {result['id']}")
            print(f"Title: {result['title']}")

        else:
            print(f"\n❌ Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Network error: {e}")


# Run the interactive example
create_post_interactive()
```

### Example 6: Sending Different Types of Data

Here's how to handle different data formats:

```python
import requests


def create_user():
    """Create a new user with more complex data structure"""
    url = "https://jsonplaceholder.typicode.com/users"

    # Complex data with nested objects
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "zipcode": "12345"
        },
        "phone": "555-1234",
        "website": "johndoe.com",
        "company": {
            "name": "Doe Industries",
            "catchPhrase": "Making things happen"
        }
    }

    try:
        response = requests.post(url, json=user_data)

        if response.status_code == 201:
            new_user = response.json()
            print("User created successfully!")
            print(f"User ID: {new_user['id']}")
            print(f"Name: {new_user['name']}")
            print(f"Email: {new_user['email']}")
            print(f"City: {new_user['address']['city']}")

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


create_user()
```

## Understanding POST Requests

### Key Differences from GET:

- **GET**: Asks for data ("Give me information")
- **POST**: Sends data ("Here's new information to save")

### Important Concepts:

#### 1. Status Codes for POST

- **201**: Created - your data was successfully saved
- **400**: Bad Request - there's something wrong with your data
- **422**: Unprocessable Entity - data format is wrong

#### 2. Content-Type Header

```python
headers = {
    "Content-Type": "application/json"
}
```

This tells the server "I'm sending JSON data"

#### 3. Two Ways to Send JSON Data

**Method 1: Using json parameter (recommended)**

```python
response = requests.post(url, json=data)
```

**Method 2: Using data parameter**

```python
import json

response = requests.post(url, data=json.dumps(data), headers=headers)
```

### Example 7: Complete CRUD Operations

Here's a simple example showing Create, Read, Update basics:

```python
import requests


class SimplePostManager:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/posts"

    def create_post(self, title, body, user_id=1):
        """Create a new post"""
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(self.base_url, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error creating post: {response.status_code}")
            return None

    def get_post(self, post_id):
        """Get a specific post"""
        url = f"{self.base_url}/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting post: {response.status_code}")
            return None


# Example usage
manager = SimplePostManager()

# Create a new post
print("Creating a new post...")
new_post = manager.create_post(
    title="Learning APIs",
    body="I'm learning how to use REST APIs with Python!"
)

if new_post:
    print(f"Created post with ID: {new_post['id']}")

    # Now get it back
    print("\nRetrieving the post...")
    retrieved_post = manager.get_post(new_post['id'])

    if retrieved_post:
        print(f"Retrieved: {retrieved_post['title']}")
```

## Common POST Request Patterns

### Pattern 1: Form-like Data

```python
# When sending simple form data
user_input = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}
response = requests.post(url, json=user_input)
```

### Pattern 2: Validation and Error Handling

```python
def safe_post_request(url, data):
    """POST request with comprehensive error handling"""
    try:
        response = requests.post(url, json=data, timeout=10)

        if response.status_code == 201:
            return True, response.json()
        elif response.status_code == 400:
            return False, "Bad request - check your data format"
        elif response.status_code == 422:
            return False, "Invalid data - check required fields"
        else:
            return False, f"Unexpected error: {response.status_code}"

    except requests.exceptions.Timeout:
        return False, "Request timed out"
    except requests.exceptions.ConnectionError:
        return False, "Connection failed"
    except Exception as e:
        return False, f"Unexpected error: {e}"


# Usage
success, result = safe_post_request(url, my_data)
if success:
    print("Data sent successfully!")
else:
    print(f"Failed: {result}")
```

## Updating Data - PUT Requests

PUT requests are used to update existing resources. You send the complete updated object.

### Example 8: Updating a Post

```python
import requests


def update_post(post_id, new_title, new_body, user_id=1):
    """Update an existing post completely"""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    # Complete updated post data
    updated_post = {
        "id": post_id,
        "title": new_title,
        "body": new_body,
        "userId": user_id
    }

    try:
        response = requests.put(url, json=updated_post)

        if response.status_code == 200:  # 200 = Successfully updated
            result = response.json()
            print("Post updated successfully!")
            print(f"Updated title: {result['title']}")
            print(f"Updated body: {result['body']}")
            return result
        else:
            print(f"Error updating post: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


# Example usage
updated_post = update_post(
    post_id=1,
    new_title="Updated: Learning REST APIs",
    new_body="This post has been updated to show how PUT requests work!"
)
```

## Deleting Data - DELETE Requests

DELETE requests remove resources from the server.

### Example 9: Deleting a Post

```python
import requests


def delete_post(post_id):
    """Delete a post by ID"""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.delete(url)

        if response.status_code == 200:  # 200 = Successfully deleted
            print(f"Post {post_id} deleted successfully!")
            return True
        elif response.status_code == 404:
            print(f"Post {post_id} not found (maybe already deleted)")
            return False
        else:
            print(f"Error deleting post: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return False


# Example usage
success = delete_post(1)
if success:
    print("Deletion completed")
else:
    print("Deletion failed")
```

### Example 10: Complete CRUD Operations

Here's a simple class that demonstrates all four basic operations:

```python
import requests


class PostManager:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/posts"

    def create(self, title, body, user_id=1):
        """CREATE - POST request"""
        data = {"title": title, "body": body, "userId": user_id}
        response = requests.post(self.base_url, json=data)
        return response.status_code == 201, response.json() if response.status_code == 201 else None

    def read(self, post_id):
        """READ - GET request"""
        response = requests.get(f"{self.base_url}/{post_id}")
        return response.status_code == 200, response.json() if response.status_code == 200 else None

    def update(self, post_id, title, body, user_id=1):
        """UPDATE - PUT request"""
        data = {"id": post_id, "title": title, "body": body, "userId": user_id}
        response = requests.put(f"{self.base_url}/{post_id}", json=data)
        return response.status_code == 200, response.json() if response.status_code == 200 else None

    def delete(self, post_id):
        """DELETE - DELETE request"""
        response = requests.delete(f"{self.base_url}/{post_id}")
        return response.status_code == 200


# Demonstration
manager = PostManager()

print("=== CRUD Operations Demo ===")

# CREATE
success, new_post = manager.create("Test Post", "This is a test")
if success:
    post_id = new_post['id']
    print(f"✅ Created post {post_id}: {new_post['title']}")

    # READ
    success, post = manager.read(post_id)
    if success:
        print(f"✅ Read post: {post['title']}")

        # UPDATE
        success, updated = manager.update(post_id, "Updated Test Post", "This has been updated")
        if success:
            print(f"✅ Updated post: {updated['title']}")

            # DELETE
            if manager.delete(post_id):
                print(f"✅ Deleted post {post_id}")
```

## HTTP Method Summary

| Method     | Purpose              | Common Status Codes              |
|------------|----------------------|----------------------------------|
| **GET**    | Retrieve data        | 200 (OK), 404 (Not Found)        |
| **POST**   | Create new data      | 201 (Created), 400 (Bad Request) |
| **PUT**    | Update existing data | 200 (OK), 404 (Not Found)        |
| **DELETE** | Remove data          | 200 (OK), 404 (Not Found)        |

## Next Steps

Now that you understand all basic HTTP methods, you're ready to:

- Add authentication headers for secured APIs
- Integrate API calls into PyQt GUI applications
- Handle more complex data structures and error scenarios
- Build complete applications that use REST APIs as their data source

## Troubleshooting Tips

- **Import Error**: Make sure you installed requests: `pip install requests`
- **Network Errors**: Check your internet connection
- **JSON Errors**: Print the raw response first: `print(response.text)`
- **Status Code Issues**: Always check `response.status_code` before parsing JSON