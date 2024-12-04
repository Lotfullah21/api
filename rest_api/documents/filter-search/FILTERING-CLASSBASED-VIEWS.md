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
    filterset_fields = ['level','course_start_date']  # Filter by related fields
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

The fields specified in search_fields and filterset_fields should match the model fields or related model fields (when using double underscores for nested lookups). They do not need to match the serializer fields.

The serializer is responsible for formatting the output and may have fields not directly related to the model.

These fields cannot be used in search_fields or filterset_fields because the filtering/searching logic works directly on the queryset.

### Example Query Strings:

###### Filter

```ruby
GET /courses/list/?level=easy
GET /courses/list/?course_start_date=2024-12-01

```

##### Search by course_name or slug

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

| **Aspect**        | **Search**                                   | **Filter**                                                            |
| ----------------- | -------------------------------------------- | --------------------------------------------------------------------- |
| **Purpose**       | To search text-based fields for a keyword    | To filter records based on exact or range values for specific fields  |
| **Use Case**      | Finding records that contain a keyword       | Narrowing down results based on specific criteria (e.g., level, date) |
| **Matching Type** | Text-based "contains" or "icontains"         | Exact matching or range-based (e.g., exact, gte, lte, in)             |
| **Flexibility**   | Searches multiple fields for partial matches | Filters based on specific fields and conditions                       |
| **Example Query** | `/courses/?search=python`                    | `/courses/?level=easy&subject=python`                                 |

`search_fields` option in Django Rest Framework (DRF), it refers to the fields of the model specified in the queryset. If we have multiple models with similar fields like title and description, the search fields will apply to the fields within the model we are working with, as defined in serializer_class.

For example, in CourseList view, the search query /courses/?search=python will search the title and description fields of the Course model because we've specified them in the search_fields for that view.

for different models like Course, Lesson, Module, etc., and each of them has title and description fields, we need to specify the search_fields separately in each view or serializer.

## Foreign Key relationships

Now, let's say we want to look for subject's title course model, then `model__query` have to be used.
