# cvaldez/tracker/tools.py
# Carlos Valdez
#
# These are tools for the Project Status Tracker.
import psycopg2
import os
import time


class ProjectNotFoundError(Exception):
    ...


class UpdateNotFoundError(Exception):
    ...


class Update:
    def __init__(self, info: tuple):
        self.project_id = info[0]
        self.version = info[1]
        self.timestamp = info[2]
        self.description = info[3]

    @staticmethod
    def create(project_id: str, version: str, description: str) -> 'Update':
        with psycopg2.connect(os.getenv('DB_LINK')) as con:
            cur = con.cursor()

            cur.execute('SELECT * FROM pst_project;')
            count = str(len(cur.fetchall()))

            cur.execute(
                "INSERT INTO pst_update(project_id, version, timestamp, description) VALUES(%s, %s, %s, %s,)",
                (project_id, version, str(time.time()), description,))

            cur.commit()

            return Update(*cur.fetchall()[0])


class Project:
    def __init__(self, uuid=None, name=None):
        assert uuid or name, "Project.__init__: UUID or name is required to find a project."

        p = get_project(uuid=uuid, name=name)

        self.name = p[0]
        self.description = p[1]
        self.id = p[2]
        self.version = p[3]
        self.last_updated = p[4]
        self.link = p[5]
        self.icon = p[6]
        self.status = p[7]
        self.release_notes: get_updates(p[2])
        self.process = {
            "requirements": p[8],
            "design": p[9],
            "code": p[10],
            "updates": p[11]
        }

    @staticmethod
    def create(name: str, desc: str) -> 'Project':
        with psycopg2.connect(os.getenv('DB_LINK')) as con:
            cur = con.cursor()

            cur.execute('SELECT * FROM pst_project;')
            count = str(len(cur.fetchall()))

            cur.execute(
                "INSERT INTO pst_project(name, description, id, version, last_update, link, icon, status, requirements, design, code, updates) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (name, desc, count, None, None, None, 'building.svg', '1', None, None, None, None,))

            cur.commit()

            return Project(count)


def create_project(name: str, description: str) -> Project:
    return Project.create(name, description)


def get_project(uuid=None, name=None) -> tuple:
    """
    Find a project inside the database.

    :param uuid: The UUID of the project
    :param name: The name of the project, case-sensitive
    :return: A tuple representing a row in the database
    """
    assert uuid or name, "get_project: UUID or name is required to find a project."

    with psycopg2.connect(os.getenv("DB_LINK")) as con:
        cur = con.cursor()
        if uuid:
            cur.execute('SELECT * FROM projects WHERE uuid=%s;', (uuid,))
        else:
            cur.execute('SELECT * FROM projects WHERE name=%s;', (name,))

        rows = cur.fetchall()
        if len(rows) == 1:
            return rows[0]
        else:
            raise ProjectNotFoundError()


def get_updates(project_id: str) -> list:
    """
    Finds updates for a project.

    :param project_id: The Project ID
    :return: A tuple
    """
    with psycopg2.connect(os.getenv('DB_LINK')) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM pst_updates WHERE uuid=%s', (project_id,))

        rows = cur.fetchall()
        if len(rows) >= 1:
            return [Update(*row) for row in rows]
        else:
            raise UpdateNotFoundError
