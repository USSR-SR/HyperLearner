from django.http.response import JsonResponse
from django.http.request import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *;
from .models import Course
# from .serializers import CourseSerializer

def CourseToDict(Course):
    output={}
    output["id"]=Course.id
    output["name"]=Course.name
    output["parts"]=Course.parts
    output["subject"]=Course.subject
    output["author"]=Course.id
    return output
def jsonMaker():
    Courses=Course.objects.all()
    temp=[]
    for i in Courses:
        temp.append(CourseToDict(i))
    return JsonResponse(temp,safe=False,status=status.HTTP_200_OK)
@api_view(['GET'])
def getAllCourses(request: HttpRequest):
    try:
        return jsonMaker()
    except ObjectDoesNotExist:
        return JsonResponse({'report': 'does not exist'}, status=status.HTTP_200_OK)
    except KeyError:
        return JsonResponse({'error': 'incomplete request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createCourse(request:HttpRequest):
    try:
        courseSerializer=CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return JsonResponse(courseSerializer.data,status=status.HTTP_200_OK)
    except:
        return JsonResponse(courseSerializer.errors,status=status.HTTP_400_BAD_REQUEST)