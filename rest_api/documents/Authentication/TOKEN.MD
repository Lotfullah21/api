## Password based authentication

with password based authentication, the client needs to send it's user name and password for every API call.

## Token based authentication

here, users send their username and password once and if they are validated, the sever generate a unique piece of string. the token will `long, hard to read, alphanumerical characters, symbols and an expiration data`.

- when client sends a new API request, it will be included in the header.s
- server checks if the token is valid or expired.
- match the user with token

the token is validated on behalf of `TokenAuthentication` class provided by `DRF`.

### How to initialize

add the following in `settings.py`

```py
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
```

Now, let's create a view and only allow authenticated users.

```py
#views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"some secret message"})
```

```py
# urls.py
urlpatterns = [
    path("course-items/",Courses.as_view(),name="course_view"),
    path("secret/",secret,name="secret_view")
]
```

Now, only authenticated users have access to the `secret` API.

We need to tell `DRF` to use `TokenAuthentication`. to do so, add the following snippet the `settings.py`

```py
#settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.TokenAuthentication',],
}
```

Now create a super user for admin panel and generate a token for a user. in insomnia, when making a request, from `Auth`, choose `Bearer token` and in token place holder, paste the token you copied from admin panel and for prefix, write `Token`.

Now, authentication tokens are sent as `Authorization: Token pasted-token`.

## User groups

In an app, we could have different kind of users, and all the users cannot have the same role or access to our resources. for instance, we want certain routes to be accessible only to the managers or admins and certain routes only for students.

when creating a user from admin panel, create different groups and place different user in different groups.

`if request.user.groups.filter(name="Instructors").exists():`, we can check if a particular user belongs to a certain group or not and based on take necessary actions.

```py
@api_view()
@permission_classes([IsAuthenticated])
def teachers_view(request):
    if request.user.groups.filter(name="Instructors").exists():
        return Response({"message":"Only for instructors only!!!"})
    else:
        return Response({"message":"You does not belong to Instructor group"}, 403)
```

Now create users in admin and put them in different groups, based on which group they belongs to, show them a different message.

### Token generation using API end point.

If the user already created, use the following routes to create a token for them
in insomnia, add the following `URL` and choose the body, post method and in the body, add the following details of the user, note that the user should be registered in our database.

add the following to `urls.py`

```py
# rest_api/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
```

```text
<!-- Body -->
username: value
password: password
```

```url
<!-- url -->
http://127.0.0.1:8000/api/api-token-auth/
```

Now, generate the token and with those token try access the following url.

```url
http://127.0.0.1:8000/api/teachers_view/
```
