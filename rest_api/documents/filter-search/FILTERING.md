## Filtering

filtering is a process that allows client applications to get a subset of results from our `API` based on some criteria.

#### Two ways to handle

### Client does the filtering

From server, send all the data and client will apply the filtering on the data

### Server sends the filtered data

Process the conditions in backend and deliver the results matching client's criteria

- the first approach does not need much logic but it puts heavy load on the server, for instance we need 10 data instances and by sending all data, heavy load is applied on the server.

- in second approach, we are putting less load on the server and making the work of client easy

### Example 1:

Lets filter the data based on the title, if title is present in query params, return the data that contains exactly that title.

we can get access to query params using `request.query_params.get("query-name")`

this is how we pass the query params, at the end of `URL`, add a `?` and after that the query parameter.

`http://127.0.0.1:8000/api/courses-items/?title=algebra`

```py

class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        course_title = request.query_params.get("title")
        if course_title:
            # get the courses that their tile matches to query params
            courses = courses.filter(title = course_title)
        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data)
```

if you want to query with more that one parameter, use `&` between the parameters
`http://127.0.0.1:8000/api/courses-items/?title=algebra&price=400`, now it query our database based on price and title

```py
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        course_title = request.query_params.get("title")
        to_price = request.query_params.get("price")
        if course_title:
            courses = courses.filter(title__icontains = course_title)
        if to_price:
            courses = courses.filter(price__lte=to_price)

        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data)
```

## Crucial point

If you want to query to a related model, for instance a model that has relationship to the model we are querying or filtering, use this format to filter.

`courses = courses.filter(modelName__fieldName = queryVariable)`
for instance, we are having model that has a one-to-many or many-to-one to the model we are filtering, then we say, filter the original model based on query value that matches with the related model

```py
from django.db import models
class Category(models.Model):
    slug = models.SlugField()
    title  = models.CharField(max_length=120)
    def __str__(self):
        return self.title
class Course(models.Model):
    title = models.CharField(max_length=120)
    instructor = models.CharField(max_length=120)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
```

```py
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        category_title = request.query_params.get("title")
        if course_title:
            courses = courses.filter(category__title = course_title)
```

generally, the template for filtering is `courses = courses.filter(fieldName__condition = queryVariable)`.

`http://127.0.0.1:8000/api/courses-items/?title=algebra`,

#### Contains the value

for instance we can use `courses = courses.filter(title__contains = queryVariable)`, it returns all data that contains `algebra` in it.
to make it case-insensitive, we use `icontains`.

#### Start with the value

for instance we can use `courses = courses.filter(title__startswith = queryVariable)`, it returns all data that contains `algebra` in it.
to make it case-insensitive, we use `istartswith`.

#### comparison

```py
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        to_price = request.query_params.get("price")
        if to_price:
            courses = courses.filter(price__lte=to_price)
```

- `courses = courses.filter(price__lte=to_price)` is used to filter the price that are less than the price.
- `courses = courses.filter(price__gte=to_price)` is used to filter the price that are larger than the price.
