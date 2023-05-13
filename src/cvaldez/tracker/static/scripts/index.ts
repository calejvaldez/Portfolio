// index.ts
// Carlos Valdez
// 
// Some tools that will be needed for the Tracker.
let div_project = document.getElementById('projects');


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

function buildProject(data: Project): HTMLAnchorElement {
    // Builds all the HTML elements to create a project container.

    // Creating the clickable
    let a = document.createElement('a');
    a.className = 'project-clickable';

    if (data.link) {
        a.href = data.link;
    }
    

    // creating the container
    let container = document.createElement('div');
    container.className = 'project-container';

    // project status
    let status = document.createElement('div')
    let status_p = document.createElement('p');

    if (data.status == '1') {
        status.className = 'project-status-req';
        status_p.textContent = 'Planning...';
    } else if (data.status == '2') {
        status.className = 'project-status-design';
        status_p.textContent = 'Designing...';
    } else if (data.status == '3') {
        status.className = 'project-status-code';
        status_p.textContent = 'Developing...';
    } else {
        status.className = 'project-status-done';
        status_p.textContent = 'Maintaining';
    }

    status.appendChild(status_p);

    // creating image
    let img = document.createElement('img');
    img.className = "img";
    img.src = `static/images/${data.icon}`;
    img.height = 150;
    img.width = 150;
    img.alt = `${data.name} logo`;

    // creating text/version
    let text = document.createElement('div');
    text.className = 'desc-text';
    let title = document.createElement('h3');
    title.textContent = data.name;
    let v = document.createElement('p');
    v.textContent = `(${data.version})`;
    v.className = 'v-desc-text';
    text.appendChild(title);
    text.appendChild(v);

    // description
    let desc = document.createElement('p');
    desc.textContent = data.description;

    // finalizing
    container.appendChild(status);
    container.appendChild(img);
    container.appendChild(text);
    container.appendChild(desc);
    a.appendChild(container);

    return a
    
};

// This is a sample of what the API would return
const sample_data: Project = {
    name: "Carlos' Portfolio",
    description: "View the status of all of Carlos' projects.",
    id: "2",
    version: "Preview",
    last_updated: "",
    link: "https://cvaldez.dev/tracker/",
    icon: "tracker.svg",
    status: "Developing",
    release_notes: [],
    process: {requirements: null, design: null, code: null, updates: null}
}

let xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let data: Array<Project> = JSON.parse(xhttp.responseText)['data'];

        data.forEach((p: Project) => {
            div_project.appendChild(buildProject(p));
        })
    }
}


xhttp.open('GET', '/api/tracker/projects/');
xhttp.send();
