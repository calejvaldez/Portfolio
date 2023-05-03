# cvaldez/tracker/tools.py
# Carlos Valdez
#
# These are tools for the Project Status Tracker.

# Demo JSON structure for a single project
demo_structure = {
    "name": "Project Status Tracker",
    "description": "View the status of all Carlos’ projects.",
    "id": 2,
    "version": "1.0B",
    "last_updated": 0,
    "link": None,
    "icon": "logo.png",
    "status": 3,
    "release_notes": [],
    "process": {"requirements": "", "design": "", "code": ""}
}


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


