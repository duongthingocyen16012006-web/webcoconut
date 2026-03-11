from flask import Flask, jsonify

app = Flask(__name__)

# trang chủ
@app.route("/")
def home():
    return "Welcome to Coconut Shop API"
@app.route("/api")
def api():
    return {"message": "Coconut API working"}
# danh sách sản phẩm
@app.route("/coconuts")
def coconuts():
    data = [
        {"id": 1, "name": "Coconut Water", "price": 20000},
        {"id": 2, "name": "Coconut Milk", "price": 30000},
        {"id": 3, "name": "Fresh Coconut", "price": 15000}
    ]
    return jsonify(data)

# đơn hàng
@app.route("/orders")
def orders():
    data = [
        {"order_id": 1, "product": "Fresh Coconut", "quantity": 2},
        {"order_id": 2, "product": "Coconut Water", "quantity": 1}
    ]
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
