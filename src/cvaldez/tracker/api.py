# cvaldez/tracker/api.py
# Carlos Valdez
#
# The API for the Project Status Tracker
# Root: https://cvaldez.dev/api/tracker/

from flask import Blueprint

bp = Blueprint('tracker api', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/api/tracker/')


@bp.route('/')
def index():
    ...
