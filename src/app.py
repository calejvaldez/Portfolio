# app.py
# Carlos Valdez

from flask import Flask
from .cvaldez import portfolio


def create_app():
    inner_app = Flask(__name__, static_folder=None)
    inner_app.register_blueprint(portfolio.views.bp)
    inner_app.register_blueprint(portfolio.api.bp)

    return inner_app


app = create_app()
