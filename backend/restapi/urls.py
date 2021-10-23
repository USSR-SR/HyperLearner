from django.conf.urls import url
from .views import getAllCourses,createCourse

urlpatterns = [
    url('^getAllCourses$', getAllCourses),
    url('^createCourse',createCourse)
]