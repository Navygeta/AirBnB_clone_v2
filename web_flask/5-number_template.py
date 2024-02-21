#!/usr/bin/env python3
"""Flask web application module"""
from flask import Flask, render_template

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def home_page():
    """Renders the homepage with a greeting"""
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Displays HBNB"""
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by custom text"""
    return "C {}".format(text)


@web_app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Displays Python followed by the text"""
    return "Python {}".format(text)


@web_app.route("/number/<int:num>", strict_slashes=False)
def number_route(num):
    """Displays the number if it's an integer"""
    return "{} is a number".format(num)


@web_app.route('/number_template/<int:num>', strict_slashes=False)
def number_template_route(num):
    """Renders an HTML page if num is an integer"""
    return render_template('5-number.html', n=num)


if __name__ == "__main__":
    web_app.run()
