#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Home page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Display C
    """
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return "Python {}".format(escape(text.replace("_", " ")))

@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """
    display n
    """
    return "{} is a number".format(n)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
