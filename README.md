# Flask MongoDB User API

A RESTful API built with Flask and MongoDB for managing user resources. This API provides endpoints for creating, reading, updating, and deleting user records with secure password hashing.

## Features

- User CRUD operations
- Password hashing for security
- Email uniqueness validation
- MongoDB integration
- Basic email format validation
- Timestamp tracking for user creation

## Prerequisites

- Python 3.x
- MongoDB installed and running locally
- Postman (for testing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhavyagp/CORIDER-ASSIGNMENT
cd CORIDER-ASSIGNMENT
```

2. Create and activate a virtual environment:

Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Ensure MongoDB is running locally on port 27017

5. Start the application:
```bash
python app.py
```

The server will start on `http://localhost:3002`

## API Endpoints

### Get All Users
- **URL**: `/user`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"users": [{"_id": "...", "name": "...", "email": "...", "password": "...", "created_at": "..."}]}`

### Get Single User
- **URL**: `/user/<id>`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"user": {"_id": "...", "name": "...", "email": "...", "password": "...", "created_at": "..."}}`
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "User not found"}`

### Create User
- **URL**: `/user`
- **Method**: `POST`
- **Data Params**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secretpassword"
  }
  ```
- **Success Response**:
  - **Code**: 201
  - **Content**: `{"message": "User created successfully"}`
- **Error Response**:
  - **Code**: 400
  - **Content**: `{"error": "Please provide name, email and password"}` or
  - **Content**: `{"error": "User with this email already exists"}` or
  - **Content**: `{"error": "Please provide a valid email"}`

### Update User
- **URL**: `/user/<id>`
- **Method**: `PUT`
- **Data Params**:
  ```json
  {
    "name": "Updated Name",
    "email": "updated@example.com",
    "password": "newpassword"
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"message": "User updated successfully"}`
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "User not found"}`

### Delete User
- **URL**: `/user/<id>`
- **Method**: `DELETE`
- **Success Response**:
  - **Code**: 200
  - **Content**: `{"message": "User deleted successfully"}`
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "User not found"}`

## Project Structure
```
project/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
└── venv/              # Virtual environment directory
```

## Required Dependencies

Create a `requirements.txt` file with the following contents:
```
flask==2.0.1
pymongo==3.12.0
werkzeug==2.0.1
```

## Testing with Postman

1. Start the Flask server
2. Open Postman
3. Use the following steps to test the endpoints:

- **Get All Users**: Create a new GET request to `http://localhost:3002/user`
- **Create New User**: Create a new POST request to `http://localhost:3002/user` with the following JSON body:
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "secretpass"
    }
    ```
- **Get Single User**: Create a new GET request to `http://localhost:3002/user/<user-id>`
- **Update User**: Create a new PUT request to `http://localhost:3002/user/<user-id>` with the following JSON body:
    ```json
    {
        "password": "Updated password"
    }
    ```
- **Delete User**: Create a new DELETE request to `http://localhost:3002/user/<user-id>`
```json
    {
       "message": "User deleted successfully" 
    }
    ```