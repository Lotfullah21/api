from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view()
def courses(request):
    return Response("list of courses provided by hooshmandlab",status=status.HTTP_200_OK)
    
    