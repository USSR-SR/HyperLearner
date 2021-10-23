from django.conf.urls import url
from .views import trial

urlpatterns = [
    url('^trial$', trial),
]