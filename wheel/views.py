from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from wheel.models import Project, Image

def index(request):

    html = ''
    project_pattern = '''
    <h1>{name}</h1>
    <h2>{desc}</h2>
    <h2>{creator}</h2>
    '''
    projects = []
    for p in Project.objects.all():
        projects.append(project_pattern.format(name=p.name, desc=p.desc, creator=p.creator))
    html = '<br>'.join(projects)

    return HttpResponse(html)