from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    database="coconut",
    user="postgres",
    password="postgres"
)

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

# đăng ký
@app.route("/register", methods=["POST"])
def register():

    data = request.json
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, phone, email) VALUES (%s,%s,%s)",
        (name, phone, email)
    )
    conn.commit()
    cur.close()

    return jsonify({"message": "Register success"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)