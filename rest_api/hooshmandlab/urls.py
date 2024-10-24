from django.urls import path
from .views import Courses, secret, teachers_view, throttle_check,throttle_check_auth
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("course-items/",Courses.as_view(),name="course_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("secret/",secret,name="secret_view"),
    path("teachers_view/",teachers_view,name="teachers_view"),
    path("throttle_check/",throttle_check,name="throttle_check_view"),
    path("throttle_check_auth/",throttle_check_auth,name="throttle_check_auth_view"),
]