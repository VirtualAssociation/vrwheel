import random
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from wheel.models import Project, Image
from wheel.forms import ProjectSubmitForm

def random_project(request):

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

def submit_project(request):
    form = ProjectSubmitForm()
    return render(request, 'wheel/submit_form.html', {'form': form})

def submit_project_ok(request):
    if request.method == 'POST':
        form = ProjectSubmitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            p = Project(name=data['name'],
                xp_type=data['xp_type'],
                desc=data['desc'],
                creator=data['creator'],
                creator_link=data['creator_url'],
                creation_date=data['creation_date'],
                needed_stuff=data['stuff'],
                submission_date=timezone.now(),
                project_link=data['url']
                )
            p.save()
            print(str(p) + ' saved')
            return render(request, 'wheel/submit_ok.html')
        else:
            print(str(form.errors))
            return render(request, 'wheel/submit_failure.html')
    return render(request, 'wheel/submit_ok.html')

