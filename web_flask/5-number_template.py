#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/hbnb')
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def is_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def is_number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Run the script"""
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
