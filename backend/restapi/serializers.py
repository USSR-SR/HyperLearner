from rest_framework import serializers
from .models import Course, Student, StudentCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
