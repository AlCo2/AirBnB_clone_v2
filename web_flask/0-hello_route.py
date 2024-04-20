#!/usr/bin/python3
# script to run flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello HBNB!"

if __name__ == '__main__':
   app.run()
