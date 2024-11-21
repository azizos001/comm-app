from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://mongodb:27017/")
db = client["ecommerce"]
products_collection = db["products"]

@app.route("/products", methods=["GET"])
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))
    return jsonify(products)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    products_collection.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
