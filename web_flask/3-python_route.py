#!/usr/bin/python3
""" script to run flask app """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ handle route / """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ handle route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """ handle route /c/<text> """
    return "C {}".format(text.replace('_', " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="cool"):
    """ handle route /python/<text> """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
