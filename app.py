from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from werkzeug.security import generate_password_hash
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

try:
    mongo_url = os.getenv("MONGODB_URL")
    client = MongoClient(mongo_url)
    db_name = os.getenv("MONG_DB_NAME")
    db = client[db_name]
    users_collection = db[os.getenv("MONGO_COLLECTION")]
except Exception as e:
    print("Error in DB connection:", e)

# Ensure unique index for email
users_collection.create_index([('email', 1)], unique=True)

# Flask routes
@app.route('/user', methods=['GET'])
def get_all_users():
    users = users_collection.find()
    output = []
    for user in users:
        user['_id'] = str(user['_id'])
        output.append(user)
    return jsonify({'users': output})

@app.route('/user/<id>', methods=['GET'])
def get_one_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify({'user': user})
    else:
        return jsonify({'error': 'User not found'})

@app.route('/user', methods=['POST'])
def create_new_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    valid_email = '@' in email and '.' in email
    if not valid_email:
        return jsonify({'error': 'Please provide a valid email'}), 400

    if not name or not email or not password:
        return jsonify({'error': 'Please provide name, email and password'}), 400

    user = users_collection.find_one({'email': email})
    if user:
        return jsonify({'error': 'User with this email already exists'}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({'name': name, 'password': hashed_password, 'email': email, 'created_at': datetime.now()})
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/user/<id>', methods=['PUT'])
def update_user_by_id(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if not user:
        return jsonify({'error': 'User not found'}), 404

    password = request.json.get('password', None)
    if password:
        hashed_password = generate_password_hash(password)
    else:
        hashed_password = user['password']

    users_collection.update_one({'_id': ObjectId(id)}, {'$set': {'password': hashed_password}})
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        users_collection.delete_one({'_id': ObjectId(id)})
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3002)
