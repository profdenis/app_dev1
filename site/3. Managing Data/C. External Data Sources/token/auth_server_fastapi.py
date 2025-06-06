#!/usr/bin/env python3
"""
Simple FastAPI Authentication Server for Educational Purposes (No External Dependencies)

This creates a basic API server with token-based authentication using only built-in Python libraries.
Perfect for educational purposes without dependency issues.

To run this server:
1. pip install fastapi uvicorn
2. python auth_server.py
3. Server will run on http://localhost:8000

API Endpoints:
- POST /login - Get authentication token
- GET /protected - Requires valid token
- GET /users/me - Get current user info (requires token)
- GET /posts - Get posts (requires token)
- POST /posts - Create post (requires token)

Test credentials:
- username: student, password: password123
- username: teacher, password: secret456
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta
import hashlib
import secrets
import base64
import json
import uvicorn

# Configuration
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Security setup
security = HTTPBearer()

# FastAPI app
app = FastAPI(
    title="Educational Authentication API",
    description="Simple API with token authentication for learning purposes (no external dependencies)",
    version="1.0.0"
)

# In-memory token storage (in production, use Redis or database)
active_tokens = {}


# Data models
class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int


class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str


class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = None


class PostCreate(BaseModel):
    title: str
    content: str


# Simple password hashing using built-in libraries
def simple_hash(password: str) -> str:
    """Simple password hashing using SHA256 - for education only!"""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return simple_hash(plain_password) == hashed_password


# Simple token creation and validation
def create_simple_token(username: str) -> tuple[str, datetime]:
    """Create a simple token using built-in libraries"""
    # Create token data
    token_data = {
        "username": username,
        "created_at": datetime.now().isoformat(),
        "expires_at": (datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).isoformat(),
        "random": secrets.token_hex(16)  # Add randomness
    }

    # Convert to JSON and encode
    token_json = json.dumps(token_data)
    token_bytes = base64.b64encode(token_json.encode()).decode()

    # Add a simple signature (in production, use proper HMAC)
    signature = hashlib.sha256(f"{token_bytes}secret_key_for_education".encode()).hexdigest()[:16]
    final_token = f"{token_bytes}.{signature}"

    expires_at = datetime.fromisoformat(token_data["expires_at"])
    return final_token, expires_at


def validate_token(token: str) -> Optional[str]:
    """Validate token and return username if valid"""
    try:
        # Split token and signature
        if '.' not in token:
            return None

        token_part, signature = token.rsplit('.', 1)

        # Verify signature
        expected_signature = hashlib.sha256(f"{token_part}secret_key_for_education".encode()).hexdigest()[:16]
        if signature != expected_signature:
            return None

        # Decode token data
        token_json = base64.b64decode(token_part.encode()).decode()
        token_data = json.loads(token_json)

        # Check expiration
        expires_at = datetime.fromisoformat(token_data["expires_at"])
        if datetime.now() > expires_at:
            return None

        # Check if token is in active tokens (for logout functionality)
        if token not in active_tokens:
            return None

        return token_data["username"]

    except (ValueError, KeyError, json.JSONDecodeError):
        return None


# Fake database with simple hashed passwords
fake_users_db = {
    "student": {
        "id": 1,
        "username": "student",
        "email": "student@example.com",
        "full_name": "Student User",
        "hashed_password": simple_hash("password123"),
    },
    "teacher": {
        "id": 2,
        "username": "teacher",
        "email": "teacher@example.com",
        "full_name": "Teacher User",
        "hashed_password": simple_hash("secret456"),
    }
}

fake_posts_db = [
    {
        "id": 1,
        "title": "Welcome to the API",
        "content": "This is a sample post in our educational API",
        "author": "teacher",
        "created_at": datetime.now() - timedelta(days=1)
    },
    {
        "id": 2,
        "title": "Learning Authentication",
        "content": "Today we learn about token-based authentication",
        "author": "teacher",
        "created_at": datetime.now() - timedelta(hours=2)
    }
]


# Utility functions
def get_user(username: str):
    """Get user from fake database"""
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return user_dict
    return None


def authenticate_user(username: str, password: str):
    """Authenticate user with username and password"""
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user from token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = credentials.credentials
    username = validate_token(token)

    if username is None:
        raise credentials_exception

    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user


# API Endpoints

@app.get("/")
async def root():
    """Welcome endpoint - no authentication required"""
    return {
        "message": "Welcome to the Educational Authentication API!",
        "docs": "Visit /docs to see all available endpoints",
        "test_credentials": [
            {"username": "student", "password": "password123"},
            {"username": "teacher", "password": "secret456"}
        ],
        "note": "This server uses simple tokens for educational purposes only!"
    }


@app.post("/login", response_model=Token)
async def login(login_request: LoginRequest):
    """
    Authenticate user and return access token

    Test with:
    - username: student, password: password123
    - username: teacher, password: secret456
    """
    user = authenticate_user(login_request.username, login_request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token
    access_token, expires_at = create_simple_token(user["username"])

    # Store token as active
    active_tokens[access_token] = {
        "username": user["username"],
        "expires_at": expires_at
    }

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60  # seconds
    }


@app.post("/logout")
async def logout(current_user: dict = Depends(get_current_user),
                 credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Logout and invalidate the current token"""
    token = credentials.credentials

    # Remove token from active tokens
    if token in active_tokens:
        del active_tokens[token]

    return {"message": "Successfully logged out"}


@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    """Protected endpoint that requires valid authentication token"""
    return {
        "message": f"Hello {current_user['full_name']}! This is a protected endpoint.",
        "user": current_user["username"],
        "access_time": datetime.now().isoformat(),
        "active_tokens_count": len(active_tokens)
    }


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    """Get current user information"""
    return User(
        id=current_user["id"],
        username=current_user["username"],
        email=current_user["email"],
        full_name=current_user["full_name"]
    )


@app.get("/posts", response_model=List[Post])
async def get_posts(current_user: dict = Depends(get_current_user)):
    """Get all posts - requires authentication"""
    return fake_posts_db


@app.post("/posts", response_model=Post)
async def create_post(post: PostCreate, current_user: dict = Depends(get_current_user)):
    """Create a new post - requires authentication"""
    new_post = {
        "id": len(fake_posts_db) + 1,
        "title": post.title,
        "content": post.content,
        "author": current_user["username"],
        "created_at": datetime.now()
    }
    fake_posts_db.append(new_post)
    return new_post


@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int, current_user: dict = Depends(get_current_user)):
    """Get a specific post by ID - requires authentication"""
    for post in fake_posts_db:
        if post["id"] == post_id:
            return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found"
    )


# Admin endpoint to see active tokens (for educational purposes)
@app.get("/admin/tokens")
async def get_active_tokens(current_user: dict = Depends(get_current_user)):
    """Get list of active tokens - for educational purposes"""
    if current_user["username"] != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access this endpoint"
        )

    # Clean up expired tokens
    current_time = datetime.now()
    expired_tokens = [token for token, data in active_tokens.items()
                      if current_time > data["expires_at"]]

    for token in expired_tokens:
        del active_tokens[token]

    return {
        "active_tokens_count": len(active_tokens),
        "tokens": [
            {
                "username": data["username"],
                "expires_at": data["expires_at"].isoformat(),
                "token_preview": token[:20] + "..."
            }
            for token, data in active_tokens.items()
        ]
    }


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "active_tokens": len(active_tokens)
    }


if __name__ == "__main__":
    print("🚀 Starting Educational Authentication API Server...")
    print("📖 Available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔑 Test credentials:")
    print("   - Username: student, Password: password123")
    print("   - Username: teacher, Password: secret456")
    print("⚡ Press Ctrl+C to stop the server")
    print("\n💡 This server uses simple tokens built with Python standard library only!")
    print("   No external JWT libraries required - perfect for education!")

    uvicorn.run(
        "auth_server_fastapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )