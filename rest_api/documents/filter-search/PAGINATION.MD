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
'PAGE_SIZE': 2
}
```
