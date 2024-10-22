## @api_view()

`@api_view()` is a decorator used to designate a view function as a RESTful API endpoint. It allows you to specify the HTTP methods that the view will accept, such as GET, POST, PUT, DELETE, etc

```py
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def courses(request):
    return Response("list of courses provided by hooshmandlab",status=status.HTTP_200_OK)
```

This is especially useful for function-based views (FBVs) when we want to restrict or handle specific HTTP methods.

- `@api_view() accepts an array of HTTP methods`: By passing a list like ['GET', 'POST'], we specify which methods the view supports.
- `Automatically handles unsupported methods`: If a method not in the list is requested, DRF will return a 405 Method Not Allowed response.
- `Access to request object`: The view gets the request object, allowing access to data like request.data for POST or request.query_params for GET.
- `Returns Response`: we use rest_framework.response.Response to return data from the view, which ensures the response is appropriately formatted as JSON or another content type supported by the framework.

By default, when we do not pass a method, it will be a get request.

```py
@api_view()
def courses(request):
    return Response("list of courses provided by hooshmandlab",status=status.HTTP_200_OK)
```

```py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def courses(request):
    if request.method == 'GET':
        data = {"message": "This is a GET request"}
        return Response(data)

    elif request.method == 'POST':
        data = {"message": "This is a POST request"}
        return Response(data)

```

It also allows us to implement throttling and rate limiting, on top of this we can also authenticate the endpoints so that only authenticated user can access.

#### function based views advantages

- Easy to implement
- Offer better readability
- easier to use the decorators
- write once-off solution quickly

## class based view

- write less code
- less code duplication
- extend and add features
- methods for HTTP request types

Here, the name of each method should be same as the http method names like, get, post, update, etc.

```py
# views.py
class Courses(APIView):
    def get(self, request):
        return Response({"messages":"list of books"}, status.HTTP_200_OK)
    def post(self, request):
        return Response({"message":"course created"}, status=status.HTTP_200_OK)

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
from django.urls import path
from .views import Courses

urlpatterns = [
    path("courses", Courses.as_view(), name="courses_view_no_slash"),
    path("courses/", Courses.as_view(), name="courses_view_with_slash"),
]
```

### Post data

`request.data.get("name")` allows to retrieve the value from a form input.

## Installing django-debug-toolbar

##### 1. installation

```sh
pip3 install django-debug-toolbar
```

##### 2. update settings.py

```py
INSTALLED_APPS = [
    # other apps
    'debug_toolbar',
]
```

```py
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # other middleware...
]
```

### 3. Configure Internal IPs

The toolbar is only displayed for specific IP addresses. Add the following configuration to the settings.py to allow it for internal IPs (like 127.0.0.1 for localhost):

```py
INTERNAL_IPS = [
    '127.0.0.1',
]
```

```py
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,  # Toolbar will be collapsed by default
}
```

#### 4. in main `urls.py`

```py
# rest_api/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("CourseListAPI.urls")),
]

# Debug toolbar URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
```
