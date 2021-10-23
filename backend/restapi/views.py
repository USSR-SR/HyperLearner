from django.http.response import JsonResponse
from django.http.request import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Course
# from .serializers import CourseSerializer


@api_view(['GET'])
def trial(request: HttpRequest):
    try:
        Course.objects.get(name=request.data['nigachu'])
        return JsonResponse({'report': 'exists'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return JsonResponse({'report': 'does not exist'}, status=status.HTTP_200_OK)
    except KeyError:
        return JsonResponse({'error': 'incomplete request'}, status=status.HTTP_400_BAD_REQUEST)
