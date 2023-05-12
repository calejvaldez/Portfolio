// index.ts
// Carlos Valdez
// 
// Some tools that will be needed for the Tracker.


// Interfaces for Update, Process, and Project that will be returned from the server.
interface Update {
    version: string
    timestamp: string
    note: string
}

interface Process {
    requirements: string
    design: string
    code: string
    updates: string
}

interface Project {
    name: string
    description: string
    id: string
    version: string
    last_updated: string
    link: string
    icon: string
    status: string
    release_notes: Array<Update>
    process: Process
}
