# cvaldez/tracker/api.py
# Carlos Valdez
#
# The API for the Project Status Tracker
# Root: https://cvaldez.dev/api/tracker/

from flask import Blueprint, request, Response
from .tools import Project, ProjectNotFoundError
import json

bp = Blueprint('tracker api', __name__,
               template_folder='templates',
               static_folder='static',
               url_prefix='/api/tracker/')


@bp.route('/project/', methods=["GET"])
def projects():
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
