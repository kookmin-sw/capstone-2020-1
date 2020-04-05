from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from settings.logger import after_request, error_handler
from settings.settings import DEBUG, POSTGRESQL


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.after_request(after_request)
    app.register_error_handler(HTTPException, error_handler)

    CORS(app)
    return app
