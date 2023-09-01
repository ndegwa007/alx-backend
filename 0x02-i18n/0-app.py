#!/usr/bin/env python3
"""this module starts a flask app"""
from flask import Flask, render_template


app = Flask(__name_)


@app.route('/')
def hello():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
