# cvaldez/tracker/tools.py
# Carlos Valdez
#
# These are tools for the Project Status Tracker.

class Project:
    def __init__(self, uuid=None, name=None):
        assert uuid or name, "Project.__init__: UUID or name is required to find a project."
        if uuid:
            ... # find from database
        elif name:
            ... # find from database

        self.name: str
        self.description: str
        self.id: int
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


