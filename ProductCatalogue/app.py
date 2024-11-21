from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products")
def get_products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Phone", "price": 500}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
