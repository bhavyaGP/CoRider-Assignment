# Flask MongoDB User API

A RESTful API built with Flask and MongoDB for managing user resources. This API provides endpoints for creating, reading, updating, and deleting user records with secure password hashing.

## Features

- Complete user CRUD operations (Create, Read, Update, Delete)
- Secure password hashing
- Email uniqueness validation
- MongoDB integration
- Basic email format validation
- Creation timestamp tracking for users
- Docker support for easy deployment

## Prerequisites

- Python 3.x
- MongoDB
- Docker (optional)
- Postman (for API testing)

## Installation

### Standard Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/flask-mongodb-api
cd flask-mongodb-api
```

2. Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure MongoDB is running on port 27017

5. Start the application:
```bash
python app.py
```

The server will start on `http://localhost:3002`

### Docker Setup

1. Build the Docker image:
```bash
docker-compose build
```

2. Run the containers:
```bash
docker-compose up
```

The API will be available at `http://localhost:3003`

## API Documentation

### 1. Get All Users
- **Endpoint**: `/user`
- **Method**: `GET`
- **Response**: 
```json
{
    "users": [
        {
            "_id": "user_id",
            "name": "name surname",
            "email": "mail@example.com",
            "created_at": "timestamp"
        }
    ]
}
```

### 2. Get Single User
- **Endpoint**: `/user/<id>`
- **Method**: `GET`
- **Success Response** (200):
```json
{
    "user": {
        "_id": "user_id",
            "name": "name surname",
            "email": "mail@example.com",
            "created_at": "timestamp"
    }
}
```
- **Error Response** (404):
```json
{
    "error": "User not found"
}
```

### 3. Create User
- **Endpoint**: `/user`
- **Method**: `POST`
- **Request Body**:
```json
{
    "name": "name surname",
    "email": "mail@example.com",
    "created_at": "timestamp"
}
```
- **Success Response** (201):
```json
{
    "message": "User created successfully"
}
```
- **Error Response** (400):
```json
{
    "error": "Please provide name, email and password"
}
```

### 4. Update User
- **Endpoint**: `/user/<id>`
- **Method**: `PUT`
- **Request Body** (all fields optional):
```json
{
    "name": "Updated Name",
    "email": "updated@example.com",
    "password": "newpassword"
}
```
- **Success Response** (200):
```json
{
    "message": "User updated successfully"
}
```

### 5. Delete User
- **Endpoint**: `/user/<id>`
- **Method**: `DELETE`
- **Success Response** (200):
```json
{
    "message": "User deleted successfully"
}
```

## Project Structure
```
project/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── docker-compose.yml  # Docker compose configuration
├── Dockerfile         # Docker configuration
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## Dependencies

```
flask==2.0.1
pymongo==3.12.0
werkzeug==2.0.1
```
