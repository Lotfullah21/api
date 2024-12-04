## Pagination

we use pagination to chunk results and instead of sending the whole data at one time, we send it in chunks.

we should also limit number of data points can be request per page.
for instance, if we set `limit=10` and the client needs 20 data points, then the client needs to make two requests.

`https/courses?perpage=10&page=4`
`https/courses?perpage=10&page=5`

if the client make a request of `perpage=40`, we need send a `bad request` response to the client.

add the following code in `views.py`

```py
from django.core.paginator import Paginator, EmptyPage

class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        perpage = request.query_params.get("perpage",default=2)
        page = request.query_params.get("page",default=1)
        paginator = Paginator(courses, per_page=perpage)
        try:
            courses = paginator.page(number=page)
        except EmptyPage:
            courses = []
        serialized_course = CourseSerializer(courses, many=True)
```

if using class based views, add the following in `settings.py`

```py
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',

    ],
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
# now 10 items per page will be served.
'PAGE_SIZE': 10
}
```

## End point

```ruby
# Get us the resource in page number 2
http://127.0.0.1:8000/courses/?page=2
```

### Pagination for Specific Class-Based View

If we want pagination only for a specific view, we can explicitly define it by overriding the pagination_class in class-based view.

```py
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import Course
from .serializers import CourseSerializer

class CoursePagination(PageNumberPagination):
     # number of results per page
    page_size = 10
    # clients to specify page size, perpage=10
    page_size_query_param = "perpage"
     # maximum page size allowed
    max_page_size = 20

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # custom pagination
    pagination_class = CoursePagination

```

```ruby
http://127.0.0.1:8000/courses/?perpage=5
```

### 5. Global Configuration (Optional)

we want to make this behavior global, set PAGE_SIZE_QUERY_PARAM in settings.py:

```py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Default page size
    'PAGE_SIZE_QUERY_PARAM': 'perpage',  # Allow query param for dynamic page size
    'MAX_PAGE_SIZE': 50,  # Optional: Maximum page size
}

```

Sometimes, the global one, especially perpage does not work but when we define the custom one, it works.
