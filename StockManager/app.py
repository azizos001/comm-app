from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://mongodb:27017/")
db = client["ecommerce"]
stock_collection = db["stock"]

@app.route("/stock/<product_id>", methods=["GET"])
def get_stock(product_id):
    stock = stock_collection.find_one({"product_id": product_id}, {"_id": 0})
    if stock:
        return jsonify(stock)
    return jsonify({"error": "Stock not found"}), 404

@app.route("/stock", methods=["POST"])
def add_stock():
    data = request.json
    stock_collection.insert_one(data)
    return jsonify({"message": "Stock added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
