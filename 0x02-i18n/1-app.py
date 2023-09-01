#!/usr/bin/env python3
"""this module starts a flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """sets language variable"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = 'UTC'


# Set the config for the flask app
app.config.from_object(Config)


@app.route('/')
def hello():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
