"""This module creates a flask website that returns the Ultraheat 50 values."""
__version__ = "0.1.0"

from flask import Flask, jsonify
from flask_caching import Cache
from werkzeug.exceptions import HTTPException

from .config import Config
from .models import UHResponse
from .ultraheat import Uh50


def create_app(config=None):
    """Creates and returns a Flask app"""
    app = Flask(__name__)

    app.config.from_object(Config)

    if config is not None:
        app.config.update(config)

    cache = Cache(app)

    @app.errorhandler(Exception)
    def handle_exception(err):
        # pass through HTTP errors
        if isinstance(err, HTTPException):
            return err

        return jsonify(error=str(err)), 500

    @app.route("/", methods=["GET"])
    @cache.cached()
    def root():
        myuh50 = Uh50(app.config["PORT"])
        data = myuh50.readdata()
        uhresponse = UHResponse.from_uh50_data(data)
        return jsonify(uhresponse.dict())

    return app
