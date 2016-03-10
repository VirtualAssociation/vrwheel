import random
import time

from django.shortcuts import render
from django.http import HttpResponse

from wheel.models import Project, Image

def index(request):

    random.seed(time.time())

    projects = Project.objects.all()
    proj = random.choice(projects)

    project_view = '''
    <h1 class="project-name">{name}</h1>
    <h2 class="project-type">{xp_type}</h2>
    <p class="project-desc">{desc}</p>
    <h2 class="project-creator">Created by <a href="{creatorlink}">{creator}</a> in {creationdate}</h2>
    <h2 class="project-stuff">Needed stuff : {stuff}</h2>
    <a href="{projectlink}">View Project</a>
    '''

    project_view = project_view.format(
        name=proj.name,
        xp_type=proj.xp_type,
        desc=proj.desc,
        creatorlink=proj.creator_link,
        creator=proj.creator,
        creationdate=str(proj.creation_date),
        stuff=str(proj.needed_stuff),
        projectlink=proj.project_link
        )

    return HttpResponse(project_view)