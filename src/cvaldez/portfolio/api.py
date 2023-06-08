# cvaldez/portfolio/api.py
# Carlos Valdez
#
# The API for my portfolio
# Root: https://cvaldez.dev/api/portfolio/

from flask import Blueprint, Response
from .portfolio import get_all_projects
import json

bp = Blueprint('portfolio api', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/api/portfolio/')


@bp.route('/projects/', methods=['GET'])
def projects():
    return Response(json.dumps({
        "data": [{
            "name": p.name,
            "description": p.description,
            "id": p.id,
            "status": p.status,
            "version": p.version if p.version is not None else 'Preview',
            "icon": p.icon,
            "link": p.link
        } for p in get_all_projects()]
    }), status=200)
