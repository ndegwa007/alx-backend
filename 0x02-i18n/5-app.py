#!/usr/bin/env python3
"""
module starts a flask application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """sets language variable"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the config for the flask app
app.config.from_object(Config)


def get_user():
    """user checker based on ID"""
    login_as = request.args.get('login_as')
    if not login_as:
        return None
    user_id = int(login_as)
    if user_id not in users:
        return None
    return users[user_id]


@app.before_request
def before_request():
    """check if user exists and set as global"""
    user = get_user()
    if user is not None:
        g.user = user['name']


@babel.localeselector
def get_locale():
    """specifies client locale and language preference"""
    user = get_user()
    g.user_locale = user['locale']
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    elif g.user_locale is not None and \
            g.user_locale in app.config['LANGUAGES']:
        return g.user_locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """flush template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
