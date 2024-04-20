#!/usr/bin/python3
""" script to run flask app """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """ handle route / """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ handle route /hbnb """
    return "HBNB"


@app.route('/c/<text>')
def c_isfum(text):
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
