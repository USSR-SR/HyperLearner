from rest_framework import serializers
from .models import Course, Student, StudentCourse,FlashCard


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= '__all__'
class FlashCardSerializer(serializers.ModelSerializer):
    # name=serializers
    class Meta:
        model=FlashCard
        fields='__all__'