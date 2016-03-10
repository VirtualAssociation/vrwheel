import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    xp_type = models.CharField(max_length=200)
    desc = models.TextField()
    creator = models.CharField(max_length=200)
    creator_link = models.CharField(max_length=200)
    creation_date = models.DateField()
    needed_stuff = models.CharField(max_length=200)
    submission_date = models.DateField()
    project_link = models.CharField(max_length=200)

    def is_hot(self):
        return self.submission_date > timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=200)
    # data = models.ImageField()






