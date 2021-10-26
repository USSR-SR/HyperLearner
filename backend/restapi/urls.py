from django.conf.urls import url
from .views import getAllCourses,createCourse,createStudent,login,addFlash,getAllStudent,AddSubjectToStudent,modifyProgressBar,me,check,login2

urlpatterns = [
    url('^getAllCourses$', getAllCourses),
    url('^createCourse',createCourse),
    url('^createStudent', createStudent),
    url('^login$',login),
    url('^addFlash',addFlash),
    url('^getAllStudent', getAllStudent),
    url('^LinkCourse', AddSubjectToStudent),
    url('^AddProgress', modifyProgressBar),
    url('^me', me),
    url("^check",check),
    url("^loda",login2)
]