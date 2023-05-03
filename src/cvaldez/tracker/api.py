from flask import Blueprint

bp = Blueprint('tracker api', __name__,
               template_folder='templates',
               static_folder='static')


@bp.route('/')
def index():
    ...
