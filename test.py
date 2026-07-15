from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

users = []
print()
def add_user(name, age):
    users.append({
        "name": name,
        "age": age
    })
    return True

def get_user(name):
    for user in users:
        if user["name"] == name:
            return user
    return None

def query_user(user_id):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    sql = "select * from users where id=" + user_id
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    name = data.get("name")
    age = data.get("age")

    add_user(name, age)

    return jsonify({
        "status": "ok"
    })

@app.route("/user/<name>")
def user_detail(name):
    user = get_user(name)

    return jsonify(user)

@app.route("/search")
def search():
    user_id = request.args.get("id")
    result = query_user(user_id)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
