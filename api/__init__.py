from flask import Flask

from api.reports import reports_api
from api.status import status_blueprint

def create_app() -> Flask:
    """
    Creates an application instance to run
    :return: A Flask object
    """

    app = Flask(__name__)

    app.register_blueprint(status_blueprint)
    app.register_blueprint(reports_api)

    return app