// index.ts
// Carlos Valdez
// 
// Some tools that will be needed for the portfolio.
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
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
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
    text.appendChild(title);

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

let xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let data: Array<Project> = JSON.parse(xhttp.responseText)['data'];

        data.forEach((p: Project) => {
            div_project.appendChild(buildProject(p));
        })
    }
}


xhttp.open('GET', '/api/portfolio/projects/');
xhttp.send();
