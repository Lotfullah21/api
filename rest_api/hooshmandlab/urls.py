from django.urls import path
from .views import Courses

urlpatterns = [
    path("course-items/",Courses.as_view(),name="course_view")
]

