#!/usr/bin/python3

"""
Simple Flask web application.

This application listens on 0.0.0.0, port 5000, and has three routes.
The route ("/") displays the message "Hello HBNB!".
The route ("/hbnb") displays the message "HBNB".
The route ("/c/<text>") displays "C" followed by the value of the text variable.

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
    """Display "HBNB" on the "/hbnb" route."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    Display 'C' followed by the value of the text variable.

    Args:
        text (str): The text variable extracted from the URL.

    Returns:
        str: A string containing 'C' followed by the formatted text.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == '__main__':
    app.run()
