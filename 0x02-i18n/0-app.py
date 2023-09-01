#!/usr/bin/env python3

"""
module starts a flask application
"""

from flask import Flask, render_template

# instantiate flask app
app = Flask(__name__)


@app.route('/')
def hello():
    """flush template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """run the app"""
    app.run()
