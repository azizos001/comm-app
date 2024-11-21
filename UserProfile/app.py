from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://mongodb:27017/")
db = client["ecommerce"]
users_collection = db["users"]

@app.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    users_collection.insert_one(data)
    return jsonify({"message": "User created successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
