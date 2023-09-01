#!/usr/bin/env python3
"""
module starts a flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """sets language variable"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the config for the flask app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """specifies client locale and language preference"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """flush template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
