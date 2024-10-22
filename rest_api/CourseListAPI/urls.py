from django.urls import path
from .views import Courses, Course

urlpatterns = [
    path("courses", Courses.as_view(), name="courses_view_no_slash"),  
    path("courses/", Courses.as_view(), name="courses_view_with_slash"),  
    path("courses/<int:pk>", Course.as_view(), name="courses_view_with_slash"),
]
