#!/usr/bin/python3
"""
Starting a Flask app.
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
