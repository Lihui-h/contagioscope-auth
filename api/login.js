const { createApiHandler } = require('@vercel/node');

module.exports = createApiHandler(async (req, res) => {
  // CORS配置
  res.setHeader('Access-Control-Allow-Origin', 'https://lihui-h.github.io');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // 处理预检请求
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // 验证逻辑
  if (req.method === 'POST') {
    const { username, password } = req.body;
    const validUser = process.env.HOSPITAL_USER;
    const validPass = process.env.HOSPITAL_PASS;

    if (username === validUser && password === validPass) {
      return res.json({
        success: true,
        redirect: "https://medical-research-profile-ke2ztwqjq7z585fuompiq4.streamlit.app/"
      });
    }
    
    return res.status(401).json({
      success: false,
      error: "机构代码或安全密钥错误"
    });
  }

  return res.status(405).end(); // Method Not Allowed
});