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

By default, when we do not pass a method, it will be a `get` request.

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
        data = {"message": "This is a GET request for courses"}
        return Response(data)

    elif request.method == 'POST':
        data = {"message": "This is a POST request for courses"}
        return Response(data)

```

It also allows us to implement throttling and rate limiting, on top of this we can also authenticate the endpoints so that only authenticated user can access.

#### function based views advantages

- Easy to implement
- Offer better readability
- easier to use the decorators
- write once-off solution quickly
