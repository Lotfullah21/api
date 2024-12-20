from CourseListAPI.models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .throttles import FiveCallsPerMinute
# Create your views here



class Courses(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    MAX_PER_PAGE = 10
    def get(self, request):
        courses = Course.objects.all()
        course_title = request.query_params.get("title")
        to_price = request.query_params.get("price")
        ordering = request.query_params.get("ordering")
        perpage = min(int(request.query_params.get("perpage", 2)), self.MAX_PER_PAGE)
        page = request.query_params.get("page",default=1)
        
        
        if course_title:
            courses = courses.filter(title__icontains = course_title)
        if to_price:
            courses = courses.filter(price__lte=to_price)
        if ordering:
            # split and grab the values from ordering
            order_values = ordering.split(",")
            # pass them all
            courses = courses.order_by(*order_values)
        paginator = Paginator(courses, per_page=perpage)
        try:
            courses = paginator.page(number=page)
        except EmptyPage:
            courses = []
        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data)
    

    def post(self,request):
        data = request.data
        serialized_data = CourseSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"message":"data created successfully"}, status=201)
        return Response({"message": "data cannot be saved", "errors": serialized_data.errors}, status=400)

        
        
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"some secret message"})
        
@api_view()
@permission_classes([IsAuthenticated])
def teachers_view(request):
    if request.user.groups.filter(name="Instructors").exists():
        return Response({"message":"Only for instructors only!!!"})
    else:
        return Response({"message":"You does not belong to Instructor group"}, 403)
    
@throttle_classes([AnonRateThrottle])
@api_view()
def throttle_check(request):
    return Response({"message": "From throttling"})

@api_view()
@throttle_classes([FiveCallsPerMinute])
@permission_classes([IsAuthenticated])
def throttle_check_auth(request):
    return Response({"message": "From authenticated throttling"})