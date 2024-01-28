#!/usr/bin/python3
"""This module returns hello world on the / route"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Returns hello world on the / route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB!'


if __name__ == '__main__':
    """Run the Flask app on 0.0.0.0, port 5000"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
