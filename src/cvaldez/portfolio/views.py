from flask import Blueprint, render_template

bp = Blueprint('portfolio', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/portfolio/')


@bp.route('/')
def index():
    return render_template("index.html")
