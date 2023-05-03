# Tracker API Docs
> WARNING: This is a draft. Things WILL change without announcement.

Welcome to the Project Status Tracker API documentation. This will be the guide for the development of the Tracker.

Root: `https://cvaldez.dev/api/tracker/`

## Authorization
This project will be integrated with the Access Protocol.

For the majority of `GET` requests, you don't need authorization! However, for `POST` or `DELETE` requests, you will need an Access 
token for a type `ADMIN` account.

## `GET /project/`
Gets the details of a project. `uuid` OR `name` is required.<br>
**Headers**

| Name       | Required? | Description                                         |
|------------|-----------|-----------------------------------------------------|
| `uuid`     | No        | The Project UUID.                                   |
| `name`     | No        | The Project name, case sensitive                    |
| `detailed` | No        | How detailed should it be? If empty, will be brief. |

**Return**

(Detailed)
```json
{
  "name": "Project Status Tracker",
  "description": "View the status of all Carlos’ projects.",
  "id": 2,
  "version": "1.0 B1",
  "last_updated": null,
  "link": null,
  "icon": null,
  "status": 3,
  "release_notes": [
    {
      "version": "1.0 B1",
      "timestamp": null,
      "note": "This is the first beta version of the Project Status Tracker. Welcome, testers!"
    }
  ],
  "process": {
    "requirements": "https://github.com/calejvaldez/ProjectTracker/blob/main/.github/PROPOSAL.md",
    "design": "https://www.figma.com/file/ErxsYnA3EkWi1ZfjQtyaLP/Tracker-Design?type=design&node-id=0%3A1&t=SfwfCIZ54tMGG0Pc-1",
    "code": "https://github.com/calejvaldez/ProjectTracker/"
  }
}
```

(Brief)
```json
{
  "name": "Project Status Tracker",
  "description": "View the status of all Carlos’ projects.",
  "id": 2,
  "status": 3,
  "version": "1.0 B1"
}
```

## `POST /project/`
Sends updated information about a project. Requires type `ADMIN` Access account.<br>
Requires a header of `uuid` AND one of the keys from the detailed version of the JSON with a value of the update.

## `DELETE /project/`
Deletes a project. Requires type `ADMIN` Access account.
Requires a `uuid`.