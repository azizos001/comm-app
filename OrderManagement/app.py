from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://mongodb:27017/")
db = client["ecommerce"]
orders_collection = db["orders"]

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    orders_collection.insert_one(data)
    return jsonify({"message": "Order created successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
