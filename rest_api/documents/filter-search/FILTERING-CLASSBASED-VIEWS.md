## Filtering in class based views

### Install `django-filter`

```sh
pip install django-filter
```

### Update `settings.py`

```sh
REST_FRAMEWORK = {
       'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
```

### Update Your View (CourseList): Extend the view by adding filter_backends, filterset_fields, and search_fields.

```py
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_id']  # Filter by related fields
    search_fields = ['course_name', 'slug']  # Search by course name or slug

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

### Example Query Strings:

Filter by category_id

```ruby
GET /courses/list/?category_id=1

```

Search by course_name or slug

```ruby
GET /courses/list/?search=machine
```

```ruby
GET /courses/list/?search=machine learning
```

---

You can notice that we are not using `course_name` in the url, but rather search and also the searched value does not necessary to be exactly present, even if it contains an alphabet or word, still it returns those.

The search query parameter works across all fields specified in the search_fields attribute, and it uses a case-insensitive partial match by default.

### How SearchFilter Works

DRF's SearchFilter looks for query parameters named search (or as configured by SEARCH_PARAM in REST_FRAMEWORK settings).
It performs a case-insensitive search using icontains lookup, which matches substrings.

### Example

```py
search_fields = ["course_name", "slug"]
```

- This means:

- The query GET /courses/list/?search=machine learning will search for any courses where:

  - course_name contains the phrase "machine learning" (or parts of it, like "machine" or "learning").

  - slug contains the phrase "machine learning" (or parts of it).

## !Crucial

The above setting only works with `json` renderers in rest_framework.
If browsable API is necessary, follow the given step.

- add `django_filters` in the INSTALLED_APPS

```sh
INSTALLED_APPS = [
    ...
    'django_filters',
]
```
