from django.contrib import admin
from django.urls import path, include
from CourseListAPI.views import courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',courses),
    path("api/", include("CourseListAPI.urls"))
]
