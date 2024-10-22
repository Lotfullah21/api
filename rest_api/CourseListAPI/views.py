from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.

@api_view(["POST","GET"])
def courses(request):
    return Response("list of courses provided by hooshmandlab",status=status.HTTP_200_OK)
    
    
class Courses(APIView):
    def get(self, request):
        instructor = request.GET.get("instructor")
        if instructor: 
            return Response({"messages":"list of courses by "+instructor}, status.HTTP_200_OK)
        return Response({"messages":"list of courses"}, status.HTTP_200_OK)
    
    
    def post(self, request):
        title = request.data.get("title")
        return Response({"message":title + " created"}, status=status.HTTP_200_OK)
    
    
class Course(APIView):
    def get(self, request, pk):
        return Response({"message":"course with id = " + str(pk)})
    def put(self, request, pk):
        title = request.data.get("title")
        return Response({"message":title + " created"})