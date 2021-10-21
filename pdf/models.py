from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    school_percentage = models.IntegerField(default=50)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    cgpa = models.FloatField(default=5)
    skill = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    previous_work_title = models.CharField(max_length=100,default='')
    previous_work_company = models.CharField(max_length=100,default='')
    previous_work = models.TextField(max_length=1000)
    project_title = models.CharField(max_length=100,default='')
    projects = models.TextField(max_length=2000,default='')
    interests = models.TextField(max_length=1000,default='')
