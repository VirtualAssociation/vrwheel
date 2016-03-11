import random
import time
import calendar

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from wheel.models import Project, Image
from wheel.forms import ProjectSubmitForm

def random_project(request):

    random.seed(time.time())
    projects = Project.objects.all()
    proj = random.choice(projects)

    return render(request, 'wheel/project.html', {
        'name': proj.name,
        'xp_type': proj.xp_type,
        'desc': proj.desc,
        'creator_url': proj.creator_url,
        'creator': proj.creator,
        'creation_date': '{mon} {year}'.format(mon=calendar.month_name[proj.creation_date.month], year=proj.creation_date.year),
        'stuff': proj.needed_stuff,
        'url': proj.project_url
    })

def submit_project(request):
    form = ProjectSubmitForm()
    return render(request, 'wheel/submit_form.html', {'form': form})

def submit_project_ok(request):
    if request.method == 'POST':
        form = ProjectSubmitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = Project(name=data['name'],
                xp_type=data['xp_type'],
                desc=data['desc'],
                creator=data['creator'],
                creator_url=data['creator_url'],
                creation_date=data['creation_date'],
                needed_stuff=data['stuff'],
                submission_date=timezone.now(),
                project_url=data['url']
                )
            p.save()
            return render(request, 'wheel/submit_ok.html')
        else:
            print(str(form.errors))
            return render(request, 'wheel/submit_failure.html', {'errors': errors})
    return render(request, 'wheel/submit_ok.html')

