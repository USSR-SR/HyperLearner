from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    parts = models.IntegerField(default=1)
    subject = models.CharField(max_length=40)
    author = models.CharField(max_length=40)



class Student(models.Model):
    mobile_num = models.CharField(max_length=10)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40,primary_key=True)
    password = models.CharField(max_length=40)
    courses = models.ManyToManyField(Course, through='StudentCourse')


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField()


class FlashCard(models.Model):
    dataFront=models.TextField()
    dataBack=models.TextField()
    username=models.ForeignKey(Student,on_delete=models.CASCADE)
