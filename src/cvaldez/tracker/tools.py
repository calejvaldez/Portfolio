# cvaldez/tracker/tools.py
# Carlos Valdez
#
# These are tools for the Project Status Tracker.
import sqlite3
import psycopg2
import os


class ProjectNotFoundError(Exception):
    ...


class Project:
    def __init__(self, uuid=None, name=None):
        assert uuid or name, "Project.__init__: UUID or name is required to find a project."

        p = get_project(uuid=uuid, name=name)

        self.name = p.name
        self.description = p.description
        self.id = p.id
        self.version: str
        self.last_updated: float
        self.link: str
        self.icon: str
        self.status: int
        self.release_notes: list[dict]
        self.process: dict[str, str]

    @staticmethod
    def create(name: str, desc: str) -> 'Project':
        ... # add to database
        return Project(...) # uuid


def create_project(name: str, description: str) -> Project:
    return Project.create(name, description)


def get_project(uuid=None, name=None) -> Project:
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
            return Project(*rows[0])
        else:
            raise ProjectNotFoundError()
