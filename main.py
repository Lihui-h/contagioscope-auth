# main.py
import os
from flask import Flask, request, jsonify  # 缺少 jsonify 和 request 导入

app = Flask(__name__)

# 示例验证逻辑（需替换为你的实际逻辑）
VALID_USER = os.environ.get("HOSPITAL_USER", "zjszyy")
VALID_PASS = os.environ.get("HOSPITAL_PASS", "Contagio@2024")

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # 获取请求数据
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()

        if username == VALID_USER and password == VALID_PASS:
            return jsonify({
                "success": True,
                "redirect": "/dashboard"
            })
        else:
            return jsonify({
                "success": False,
                "error": "机构代码或安全密钥错误"
            }), 401

    except Exception as e:
        # 必须捕获异常，否则 Vercel 会返回 500 错误
        return jsonify({
            "success": False,
            "error": f"服务器内部错误: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))