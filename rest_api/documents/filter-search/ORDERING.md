## django-filter

a package used with class based views.

## ordering

Based on certain parameters, we can order or sort our `API` result.

For instance, sorting based on price, or length of the course name and so on. The procedure is no different than filter with few subtle difference.

- add a query parameter in the url
- if you want order based on more than one parameter, add a `,` between the parameters
- by default, the ordering is done in ascending order, from lowest to highest.
- if you want to order them in reverse order, add `-` before a query parameter

`http://127.0.0.1:8000/api/courses-items/?ordering=price`

```py
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        ordering = request.query_params.get("ordering")
        if ordering:
            courses = courses.order_by(ordering)
        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data)
```

### ordering based on multiple parameters

To order the response based on many parameters, add the `,` in between and use python `split` method to get all the parameters and `*` destructuring to pass them to `order_by` method.

`http://127.0.0.1:8000/api/courses-items/?ordering=price,title`

```py
class Courses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        ordering = request.query_params.get("ordering")
        if ordering:
            # split and grab the values from ordering
            order_values = ordering.split(",")
            # pass them all
            courses = courses.order_by(*order_values)
        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data)
```

```py
if ordering:
    # split and grab the values from ordering
    order_values = ordering.split(",")
    # pass them all
    courses = courses.order_by(*order_values)
```

`.split`: splits the string based on `,` and returns an array of them, for instance, if params are `ordering=price,title`, then `order_values=["price", "title"]`.

`courses = courses.order_by(*order_values)`: unpack the order_values array and pass them to `order_by` method. now it will be like `courses = courses.order_by("price", "title")`.

### How ordering=price,title works:

When we call the API with `?ordering=price,title`, Django will order the queryset of Course objects first by the price field (ascending by default), and then by the title field (also ascending).
This means that courses with the same price will be ordered by title.

### What happens:

- The ordering query parameter (price,title) is captured in the API view.
- It is split into a list of fields: ['price', 'title'].
- These fields are passed to order_by in Django
- Django orders the Course objects based on the specified fields in the query.
- The fields passed in the ordering parameter (e.g., price, title) must match the field names in your Course model.
- Django's order_by method operates directly on the model fields
