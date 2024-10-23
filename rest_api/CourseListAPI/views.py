from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_list_or_404

# create your views here.
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.select_related("category").all()
        print(type(courses))
        # covert a queryset to json, many=True is essential here.
        serialized_courses = CourseSerializer(courses, many=True)
        return Response(serialized_courses.data)

# create your views here.
class SingleCourse(APIView):
    def get(self, request, id):
        course = get_list_or_404(Course, pk=id)
        serialized_course = CourseSerializer(course)
        return Response(serialized_course.data)