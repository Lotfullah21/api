## URL

every single resource on web is located by an address, known as `uniform resource locator`.
url is an address where files are stored.

A URL is made up of multiple parts put together like Scheme, Domain Name, File Path, and Parameters

## Parameters

query parameters and path parameters are two ways to pass data to a web server, but they serve different purposes and are structured differently. Here's a breakdown of their differences:

a url is consist of scheme(protocol), domain, subdomain and file path.
For instance `https://amazon.com/books`

- scheme: https
- subdomain: www
- domain
  - second level domain: amazon
  - top level domain: .com
- path: books

`file path` is the location of the file and resources, now theses resources can be locally saved in our machine or web-based, stored somewhere in web.

# URL Parameters (Path parameter)

It structures additional information inside a URL.
Path parameters are part of the URL path itself, it is used to capture any part of a url, `google.com/2022/`: here, 2022 is a parameter.

`Example: https://example.com/users/123` (where 123 is the path parameter representing a specific user ID)

```py
# urls.py
from django.urls import path
from .views import get_course_path_info
urlpatterns = [
    path("course-info/<name>/<id>",get_course_path_info),
]

```

```py
# views.py
def get_course_path_info(request,name, id):
    return HttpResponse(f"course {name}  has id number: {id}")
```

# (Query Strings)

A query string is a sequence of one or more key=value pairs concatenated by the & symbol. Each key is the query parameter. The query string ends with the ? symbol after the URL endpoint.
It is the entire part of the URL that comes after the `?`.

The URL dispatcher doesn’t parse these parameters. They are fetched by the view from the request object it receives. The request object’s GET property is a dictionary object.

The key-value pairs in the query string are added to the request.GET property. Hence, the name can be obtained with `request.GET[‘name’]` expression.

`google.com/?year=2022`: here, year is a query string.

we can more than one query string by adding `&` in between.

`google.com/?year=2022&month="Oct"`

# Query parameter

Query parameter refer to the individual key-value pairs in the query string.

```py
https://example.com/search?query=apple&sort=price
```

```py
# urls.py
from django.urls import path
from .views importget_course_query_string
urlpatterns = [
    path("course-info/",get_course_query_string),
]
```

## Accessing the query params

### 1. Standard Django Approach: request.GET["param-name"]

- ##### Behavior:

- Accesses the value of a query parameter by its key.
- Throws a KeyError if the parameter is missing.

- ##### Use Case:

When the query parameter is required and must always be present in the request.

```py
# views.py
def get_course_query_string(request):
    name = request.GET["name"]  # Will raise KeyError if "name" is missing
    id = request.GET["id"]      # Will raise KeyError if "id" is missing
    return HttpResponse(f"Course {name} has ID number: {id}")

```

#### Example url

```sh
http://127.0.0.1:8000/courses/course-info/?name=machine learning&id=12

```

### Error Example:

If we omit id in the query string

```py
http://127.0.0.1:8000/courses/course-info/?name=machine learning

```

we get a KeyError: 'id'.

```py
# views.py
def get_course_query_string(request):
    name = request.GET["name"]
    id = request.GET["id"]
    return HttpResponse(f"course {name}  has id number: {id}")
```

### 2. DRF Approach: request.GET.get("param-name")

- ##### Behavior:

- Safely retrieves the value of a query parameter by its key.
- Returns None (or a default value) if the parameter is missing.

- #### Use Case:

- When the query parameter is optional or might be missing.

```py
# views.py
def get_course_query_string(request):
    course = request.GET.get("course")  # Returns None if "course" is missing
    id = request.GET.get("id")          # Returns None if "id" is missing
    return HttpResponse(f"Course {course} has ID number: {id}")

```

### Example URL:

```ruby
http://127.0.0.1:8000/courses/course-info/?course=AI&id=101

```

#### Missing Parameters:

If id is missing

```ruby
http://127.0.0.1:8000/courses/course-info/?course=AI

```

```mathematica
Course AI has ID number: None
```

Key differences

| **Aspect**                         | **Standard Django (`request.GET["key"]`)** | **DRF (`request.GET.get("key")`)**                     |
| ---------------------------------- | ------------------------------------------ | ------------------------------------------------------ |
| **Error Handling**                 | Throws `KeyError` if the key is missing.   | Returns `None` if the key is missing.                  |
| **Default Value**                  | Not supported.                             | Can specify a default value (`get("key", "default")`). |
| **Use Case**                       | Required query parameters.                 | Optional or potentially missing parameters.            |
| **Example Behavior (Key Missing)** | `KeyError: 'key'`                          | Returns `None` or default value.                       |

| Feature             | **Query String**                                                          | **Query Parameters**                                                           | **Path Parameters**                                                         |
| ------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Definition**      | The entire section after the `?` in a URL, consisting of key-value pairs. | Individual key-value pairs that make up the query string.                      | Values embedded directly in the URL path that represent specific resources. |
| **Purpose**         | To pass optional data or filters to the server.                           | To define individual pieces of optional data, like filters or search criteria. | To identify specific resources or entities (e.g., user IDs, product IDs).   |
| **Location in URL** | After the `?` symbol. Example: `?key=value&sort=asc`                      | Each `key=value` pair after the `?` and separated by `&`.                      | Inside the URL path itself. Example: `/users/123`                           |
| **Syntax**          | Starts with `?` followed by `key=value` pairs separated by `&`.           | `key=value` pairs. Each parameter is separated by `&`.                         | Typically part of the path structure with no special symbols.               |
| **Use Cases**       | Used for filtering, sorting, pagination, or search terms.                 | Filters, sorting options, pagination values (e.g., `page=2`), etc.             | Used for resource identification like `/users/{id}` or `/products/{id}`.    |
| **Example**         | `?category=fruits&sort=price`                                             | `category=fruits`, `sort=price`                                                | `/products/456`, `/users/123`                                               |

### Note:

`query parameters` for optional filters or settings and `path parameters` for identifying specific resources

# Body parameter

An HTML form sends the data to the URL mentioned in its action attribute using the POST method. The POST method is a more secure way of sending data than the GET method because the data is not revealed in the URL

```html
<form action="/courses/capture-form/" method="POST">
	{% csrf_token %}
	<p>Name: <input type="text" name="id" /></p>
	<p>UserID :<input type="name" name="name" /></p>
	<input type="submit" />
</form>
```

```py
# urls.py
from django.urls import path
from .views import show_form,capture_form

urlpatterns = [
    path("show-form/",show_form),
    path("capture-form/",capture_form)
]
```

```py
# views.py
def capture_form(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse(f"name: {name} id: {id}")
```

## Key Differences Between `request.data.get()` and `request.POST[]`

| **Aspect**            | **`request.data.get()`**             | **`request.POST[]`**                              |
| --------------------- | ------------------------------------ | ------------------------------------------------- |
| **Source**            | DRF’s request parsing                | Django’s POST form handling                       |
| **Supported Formats** | JSON, form data, multipart, etc.     | Form data (`application/x-www-form-urlencoded`)   |
| **Default Handling**  | Returns `None` if the key is missing | Raises `KeyError` (use `.get()` to return `None`) |
| **Flexibility**       | Works for APIs with various payloads | Limited to form-encoded POST data                 |

# Client error responses

- `400`: It represents a bad request, some of the params might not match what the server expects.
- `401`: For authentication, the use must logged in to be able make a request.
- `403`: Request is successful, but the user does not have required permission.
- `404`: The resource cannot be located at the specified path.

# Server error responses

It shows that a failure occurred on the web sever when trying to process the request.
For instance, application failure, long time to respond.

`500`: Server failed to process the request.

Django handles all error cases by raising an exception which is invoked via an error handler view.
We can configure it as well.
A project level `views.py` must be created handling all the errors across the project.
