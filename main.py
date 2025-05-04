# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # 新增 CORS 支持
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有域名的跨域请求

VALID_USER = os.environ.get("HOSPITAL_USER", "zjszyy")
VALID_PASS = os.environ.get("HOSPITAL_PASS", "Contagio@2024")

@app.route('/api/login', methods=['POST', 'OPTIONS'])  # 添加 OPTIONS 方法支持
def login():
    if request.method == 'OPTIONS':
        return jsonify({"status": "preflight"}), 200  # 处理预检请求
    
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if username == VALID_USER and password == VALID_PASS:
        return jsonify({"success": True, "redirect": "/dashboard"})
    else:
        return jsonify({"success": False, "error": "机构代码或安全密钥错误"}), 401

if __name__ == "__main__":
    app.run()