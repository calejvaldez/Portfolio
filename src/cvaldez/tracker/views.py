from flask import Blueprint

bp = Blueprint('tracker', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/tracker/')


@bp.route('/')
def index():
    ...
