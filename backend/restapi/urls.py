from django.conf.urls import url
from .views import getAllCourses,createCourse,createStudent,login,addFlash,getAllStudent,AddSubjectToStudent

urlpatterns = [
    url('^getAllCourses$', getAllCourses),
    url('^createCourse',createCourse),
    url('^createStudent', createStudent),
    url('^login',login),
    url('^addFlash',addFlash),
    url('^getAllStudent', getAllStudent),
    url('^LinkCourse', AddSubjectToStudent),
]