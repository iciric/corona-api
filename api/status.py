from flask import Blueprint

status_blueprint = Blueprint('status', __name__)


@status_blueprint.route('/status/')
def status():
    """
    Checks if service is running.
    """
    return {'message': 'Running'}
