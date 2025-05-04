# api/login.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 允许跨域

# 从环境变量读取凭证
VALID_USER = os.getenv("HOSPITAL_USER", "zjszyy")
VALID_PASS = os.getenv("HOSPITAL_PASS", "Contagio@2024")

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return jsonify({"status": "preflight"}), 200
    
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if username == VALID_USER and password == VALID_PASS:
        return jsonify({"success": True, "redirect": "/dashboard"})
    else:
        return jsonify({"success": False, "error": "机构代码或安全密钥错误"}), 401

# Vercel 要求的标准入口函数
def handler(request):
    return app(request)