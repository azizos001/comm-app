from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the ShopFront!"})

@app.route("/products")
def get_products():
    response = requests.get("http://productcatalogue:5000/products")
    return jsonify(response.json())

@app.route("/stock/<product_id>")
def get_stock(product_id):
    response = requests.get(f"http://stockmanager:5000/stock/{product_id}")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
