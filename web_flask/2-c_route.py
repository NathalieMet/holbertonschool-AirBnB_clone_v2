#!/usr/bin/python3
""" return HBNB
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ return Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def diplay_c_and_text(text):
    """ display “C ” followed by the value of the text variable """
    text = escape(text).replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
