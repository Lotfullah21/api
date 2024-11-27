## Restriction

Let's we want to restrict some of the methods by certain kinds of users.

### Step 1: Create a custom permission class

```py
# .permissions
from rest_framework import permissions
class IsSuperUserOrStaff(permissions.BasePermission):
    """
    Custom permission to allow only superusers or staff users
    to perform POST, PATCH, DELETE operations.
    """
    def has_permission(self, request, view):
        # allow all users to make GET requests
        if request.method == 'GET':
            return True
        # allow only superusers or staff users to make POST, PATCH, DELETE requests
        return request.user and (request.user.is_superuser or request.user.is_staff)

```

Now, we can use this permission wherever we want.

### Step 2: Apply the Custom Permission to the Views

```py
# .views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializer import CourseSerializer
from .models import Course
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsSuperUserOrStaff

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category_id"]
    search_fields = ["course_name", "slug"]
    permission_classes = [IsSuperUserOrStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            "message": "Course Created successfully!!!!",
            "course": serializer.data
        }
        return Response(response_data, status.HTTP_201_CREATED)
```

The GET request is open to all users, but POST, PATCH, and DELETE requests are restricted to superusers or staff users using the IsSuperUserOrStaff custom permission class.
DRF's permission classes give us control over which users can access which actions.
