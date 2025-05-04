# api/test.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

def handler(request):
    return app(request)