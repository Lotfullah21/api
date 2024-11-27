## Djoser

`Djoser` is a Django library that simplifies the process of setting up authentication in web applications using the Django REST Framework (DRF). It provides a set of views, serializers, and endpoints for common authentication functionalities, such as user registration, login, password reset, and token-based authentication (via JSON Web Tokens or token authentication).

### Setup for integrating `Djoser` in our app

#### 1. Installation

```py
pip install djoser
pip install filter-backends
```

#### 2. Settings configuration

```py
# settings.py

# add the djoser at the end of installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    "djoser"
]
```

Create a new section called `DJOSER` and the fields you want as primary key for authentication, it can be email, username, ..., etc.

```py
# setting.py
# add which authentication system you want
'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.TokenAuthentication',
                                      'rest_framework.authentication.SessionAuthentication'],

```

### Main url

in main `urs.py`, enable `djoser` end points.

```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("CourseListAPI.urls")),
    path("api/", include("hooshmandlab.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/",include("djoser.urls.authtoken"))
]
```

Now, login in admin page and try different routes.

```py
http://127.0.0.1:8000/auth/users/ # it will return all users
http://127.0.0.1:8000/auth/users/me
http://127.0.0.1:8000/auth/users/resend_activation
http://127.0.0.1:8000/auth/users/confirm
http://127.0.0.1:8000/auth/users/set_password
http://127.0.0.1:8000/auth/users/reset_password
http://127.0.0.1:8000/auth/users/reset_password_confirm
http://127.0.0.1:8000/auth/users/set_username
http://127.0.0.1:8000/auth/users/reset_username
http://127.0.0.1:8000/auth/users/reset_username_confirm
http://127.0.0.1:8000/token/login
http://127.0.0.1:8000/token/logout
```

## User registration with djoser.

in insomnia, visit this end point

```py
http://127.0.0.1:8000/auth/users/
```

in body provide

```text
username:value,
email: value,
password: password
```

the method should `POST` just by sending a request, we will be creating a user.
