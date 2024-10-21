from django.urls import path
from .views import courses


urlpatterns = [
    path("courses/", courses, name="courses_api")
]
