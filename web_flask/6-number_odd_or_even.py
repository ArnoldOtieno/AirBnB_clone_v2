#!/usr/bin/python3
"""
Starting a Flask app.
"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_param(text='is cool'):
    text_no_underscore = text.replace('_', ' ')
    return 'Python {}'.format(text_no_underscore)


@app.route('/number/<int:n>')
def mnumber(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        ev_od = "even"
    else:
        ev_od = "odd"
    return render_template('6-number_odd_or_even.html', ev_od=ev_od, number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
