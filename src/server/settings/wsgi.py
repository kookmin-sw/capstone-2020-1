from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import *

from api.chatlog_highlight import app as api_chatlog_highlight
from api.sound_highlight import app as api_sndhighlight
from api.predict import app as api_predict
from api.predict7 import app as api_predict7
from api.SNDnormalize import app as api_sndnormalize
from api.account import app as api_account
from api.ana_url import app as api_analysis
from api.chatlog import app as api_chatlog
from api.file import app as api_file
from api.login import app as api_login
from api.server import app as api_server
from api.test import app as api_test
from settings.logger import after_request, error_handler
from settings.settings import DEBUG, POSTGRESQL


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
    app.register_blueprint(api_chatlog)
    app.register_blueprint(api_sndnormalize)
    app.register_blueprint(api_analysis)
    app.register_blueprint(api_account)
    app.register_blueprint(api_predict)
    app.register_blueprint(api_predict7)
    app.register_blueprint(api_file)
    app.register_blueprint(api_sndhighlight)
    app.register_blueprint(api_chatlog_highlight)

    CORS(app)
    return app
