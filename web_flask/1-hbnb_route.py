#!/usr/bin/python3

"""
Simple Flask web application.

This application listens on 0.0.0.0, port 5000, and has a single route.
The route ("/") displays the message "Hello HBNB!".

Usage:
    Run this script and access the web application at http://0.0.0.0:5000/
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" on the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run()
