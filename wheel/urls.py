from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^submit_project_ok/', views.submit_project_ok, name='submit_project_ok'),
    url(r'^submit_project/', views.submit_project, name='submit_project'),
    url(r'^random_project/', views.random_project, name='random_project'),
]