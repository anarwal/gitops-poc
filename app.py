"""The is a simple python Flask app"""
from flask import Flask
APP = Flask(__name__)

@APP.route("/")
def hello():
    """This is the main page of the web application"""
    return "Hello from Python!"

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=3000)