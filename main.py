from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求（生产环境应限制域名）

@app.route('/api/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    # 示例验证逻辑（替换为你的实际逻辑）
    if data.get('username') == 'zjszyy' and data.get('password') == 'Contagio@2024':
        return jsonify({"success": True, "redirect": "/dashboard"})
    else:
        return jsonify({"success": False, "error": "认证失败"}), 401

if __name__ == '__main__':
    app.run()