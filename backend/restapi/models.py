from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=40)
    parts = models.IntegerField(default=1)


class Student(models.Model):
    mobile_num = models.CharField(max_length=10)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    courses = models.ManyToManyField(Course)
