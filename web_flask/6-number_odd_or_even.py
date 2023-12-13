#!/usr/bin/python3
"""  display a HTML page only if n is an integer
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """  display “n is a number” only if n is an integer """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_HTML_page(n):
    """  display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_(n):
    """ display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
