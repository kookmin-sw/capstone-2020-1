from api.server import app as api_server
from api.test import app as api_test
from api.login import app as api_login
from flask import Flask
from flask_cors import CORS
from settings.logger import after_request, error_handler
from settings.settings import DEBUG, POSTGRESQL
from werkzeug.exceptions import *


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.after_request(after_request)
    app.register_error_handler(InternalServerError, error_handler)

    # app connections
    app.register_blueprint(api_server)
    app.register_blueprint(api_test)
    app.register_blueprint(api_login)

    CORS(app)
    return app
