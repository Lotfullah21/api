from django.urls import path
from .views import Courses, SingleCourse

urlpatterns = [
    path("courses", Courses.as_view(), name="courses_view_no_slash"),  
    path("courses/", Courses.as_view(), name="courses_view_with_slash"),  
    path("course/<int:id>", SingleCourse.as_view(), name="single_course"),  
]
