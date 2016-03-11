from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.random_project, name='random_project'),
    url(r'^submit/', views.submit_project, name='submit_project'),
    url(r'/submit_ok/', views.submit_project_ok, name='submit_project_ok'),
]