from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.random_project, name='random_project'),
    url(r'submit/', views.submit, name='submit'),
    url(r'submit_ok/', views.submit_ok, name='submit_ok'),
]