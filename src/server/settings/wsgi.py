import time
import traceback

from flask import Flask
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from settings.settings import DEBUG, POSTGRESQL


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    return app
