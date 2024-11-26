## Class based view

It allows to get the work done faster and makes our code clean by reusing common functionalities.

#### Advantages

- write less code
- less code duplication
- extend and add features
- methods for HTTP request types

Here, the name of each method should be same as the http method names like, get, post, update, etc.

```py
# views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
class CourseList(APIView):
    def get(self, request):
        message = {"list of books"}
        return Response(message, status.HTTP_200_OK)
    def post(self, request):
        message = {"list of books from post request"}
        return Response(message, status.HTTP_201_CREATED)
```

Map the current view to an api end point.

```py
# rest_api/urls
from django.contrib import admin
from django.urls import path, include
from CourseListAPI.views import courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("CourseListAPI.urls"))
]
```

We need to add two paths, one with slash and the other one without slash, some browsers by default add the trailing slash and that makes it difficult when adding query parameters.

```py
# CourseListAPI/urls
from django.urls import path, include
from . import views
urlpatterns = [
    path("test/",views.courses, name="courses list"),
    path("test/list/",views.CourseList.as_view(), name="courses list"),
]
```

```sh
http://127.0.0.1:8000/api/test/list/
http://127.0.0.1:8000/api/test/
```

## Capturing the query parameter

`course = request.GET.get("course")`, using this code the value associated with a query parameter can be retrieved.

```py
class CourseList(APIView):
    def get(self, request):
        course = request.GET.get("course")
        message = f"course: {course} is present"
        if course:
            return Response(message, status.HTTP_200_OK)
        return Response(message, status.HTTP_200_OK)
    def post(self, request):
        message = {"list of books from post request"}
        return Response(message, status.HTTP_201_CREATED)
```

```sh
http://127.0.0.1:8000/api/test/list/?course=machine-learning

```

## Accepting form-url encoded data or json

We can accept the from url encoded data or json data in a post request and do operations on that data.
the posted data is known as `payload`.

```py
class CourseList(APIView):
    def post(self, request):
        start_date = request.data.get("start_date")
        name = request.data.get("name")
        message = f"{name} will start in {start_date}"
        return Response(message, status.HTTP_201_CREATED)
```

### Standard django approach

```py
start_date = request.POST("start_date")
name = request.POST["name"]
```

### DRF Approach

```py
start_date = request.data.get("start_date")
name = request.data.get("name")
```

## Key Differences Between `request.data.get()` and `request.POST[]`

| **Aspect**            | **`request.data.get()`**             | **`request.POST[]`**                              |
| --------------------- | ------------------------------------ | ------------------------------------------------- |
| **Source**            | DRF’s request parsing                | Django’s POST form handling                       |
| **Supported Formats** | JSON, form data, multipart, etc.     | Form data (`application/x-www-form-urlencoded`)   |
| **Default Handling**  | Returns `None` if the key is missing | Raises `KeyError` (use `.get()` to return `None`) |
| **Flexibility**       | Works for APIs with various payloads | Limited to form-encoded POST data                 |
