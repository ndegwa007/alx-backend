#!/usr/bin/env python3
"""this module starts a flask app"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "helo"


if __name__ == '__main__':
    app.run()
