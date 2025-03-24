from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_friend():
    return "Hello Friend, From simple flask application"

