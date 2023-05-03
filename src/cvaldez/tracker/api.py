from flask import Blueprint

bp = Blueprint('tracker api', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/api/tracker/')


@bp.route('/')
def index():
    ...
