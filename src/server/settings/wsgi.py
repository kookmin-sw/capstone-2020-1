from flask import Flask
from flask_cors import CORS
from settings.settings import DEBUG, POSTGRESQL
from werkzeug.exceptions import HTTPException


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    return app
