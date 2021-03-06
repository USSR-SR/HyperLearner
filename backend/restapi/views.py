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
def StudentTodict(Student):
    output={}
    output["mobile_num"]=Student.mobile_num
    output["first_name"]=Student.first_name
    output["last_name"]=Student.last_name
    output["username"]=Student.username
    output["password"]=Student.password
    return output
def jsonMakerStudent():
    Students=Student.objects.all()
    temp=[]
    for i in Students:
        temp.append(StudentTodict(i))
    return  JsonResponse(temp,status=status.HTTP_200_OK,safe=False)
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


@api_view(['POST'])
def createStudent(request:HttpRequest):
    try:
        studentSerializer=StudentSerializer(data=request.data)
        if studentSerializer.is_valid():
            studentSerializer.save()
            return JsonResponse(studentSerializer.data,status=status.HTTP_200_OK)
    except:
        return JsonResponse(studentSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getAllStudent(request:HttpRequest):
    try:
        return jsonMakerStudent()
    except:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def login(request:HttpRequest):
    try:
        res=Student.objects.get(username=request.data["username"])
        user=StudentSerializer(res)
        if(user.data.get("password")==request.data["password"]):

            return JsonResponse({"message":"Logged in "},status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"Wrong Password "},status=status.HTTP_204_NO_CONTENT)
    except:
        return JsonResponse({"message ":"not found user"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addFlash(request:HttpRequest):
    res=Student.objects.get(username=request.data['username'])
    try:
        res.flashcard_set.create(dataFront=request.data['dataFront'],dataBack=request.data['dataBack'])
        return  JsonResponse(request.data,status=status.HTTP_200_OK)
    except:
        return JsonResponse({"message ":"does not exist"},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def AddSubjectToStudent(request: HttpRequest):
    try:
        studentT=Student.objects.get(username=request.data['username'])
        subjectT=Course.objects.get(id=request.data['id'])
        studentT.courses.add(subjectT,through_defaults={'progress': 5})
        return JsonResponse({"user":studentT.username,"subject":subjectT.id},status=status.HTTP_200_OK)
    except:
        return JsonResponse({"status":"failed"},status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def modifyProgressBar(request:HttpRequest):
    try:
        studentT = Student.objects.get(username=request.data['username'])
        subjectT = Course.objects.get(id=request.data['id'])
        studentCourse=StudentCourse.objects.get(student=studentT,course=subjectT)
        studentCourse.progress+=5
        studentCourse.save()
        return JsonResponse({"progress ":studentCourse.progress},status=status.HTTP_200_OK)
    except:
        return JsonResponse({"progress ":studentCourse.progress},status=status.HTTP_200_OK)
