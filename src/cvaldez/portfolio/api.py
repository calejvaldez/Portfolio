# cvaldez/portfolio/api.py
# Carlos Valdez
#
# The API for my portfolio
# Root: https://cvaldez.dev/api/portfolio/

from flask import Blueprint, request, Response
from .tools import Project, ProjectNotFoundError, get_all_projects
import json

bp = Blueprint('portfolio api', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/api/portfolio/')


@bp.route('/project/', methods=["GET"])
def project():
    if not ("uuid" or "name" in request.headers):
        return Response({"error": "uuid or name must be in headers"}, status=400)

    try:
        if 'uuid' in request.headers:
            p = Project(uuid=request.headers['uuid'])
        else:
            p = Project(name=request.headers['name'])
    except ProjectNotFoundError:
        return Response({"error": "Could not find project."}, status=400)

    if 'detailed' in request.headers and request.headers['detailed'] == '1':
        return Response(json.dumps({
            "name": p.name,
            "description": p.description,
            "id": p.id,
            "version": p.version,
            "last_updated": p.last_updated,
            "link": p.link,
            "icon": p.icon,
            "status": p.status,
            "release_notes": [{"version": r.version, "timestamp": r.timestamp, "note": r.description} for r in p.release_notes],
            "process": p.process
        }), status=200)
    else:
        return Response(json.dumps({
            "name": p.name,
            "description": p.description,
            "id": p.id,
            "status": p.status,
            "version": p.version
        }), status=200)


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
