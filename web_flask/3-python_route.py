#!/usr/bin/python3
""" display “Python ”, followed by the value of the text variable
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def diplay_python_and_text(text="is cool"):
    """ display “Python ”, followed by the value of the text variable """
    text = escape(text).replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
