## Authentication with JWT

### Setup for integrating `JWT` in our app

#### 1. Installation

```sh
pip install djangorestframework-simplejwt
```

#### 2. Settings configuration

in `settings.py`, in two places we need to write some changes.

```py
INSTALLED_APPS = [
    "hooshmandlab",
    "djoser",
    "rest_framework_simplejwt",
]
```

add in `REST_FRAMEWORK`

```py
REST_FRAMEWORK = {
    ... rest of code
    'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.TokenAuthentication',
                                      'rest_framework.authentication.SessionAuthentication',
                                      'rest_framework_simplejwt.authentication.JWTAuthentication',
                                      ],
}
```

in main `urls.py`, add the import few libraries and add few endpoints when visited, the tokens shall be generated or refreshed.

```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("CourseListAPI.urls")),
    path("api/", include("hooshmandlab.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/",include("djoser.urls.authtoken")),
    path("api/token",TokenObtainPairView.as_view(), name="token_obtain_pair_review"),
    path("api/token/refresh/", TokenRefreshView, name="token_refresh_view")
]
# Debug toolbar URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


```

Now, let's generate some JWT token. Go to insomnia and post the username and password information of a user.

<figure>
<img src="./assets/jwt.png" alt="jwt token" height="105" width="720" />
</figure>

There are two tokens involved in jwt.

```sh
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTg1NDc5OCwiaWF0IjoxNzI5NzY4Mzk4LCJqdGkiOiI4NTJmNmFhNDdiOTI0MjJjODI0NjFiMWU5Y2ZjNGRkNCIsInVzZXJfaWQiOjR9.8-tkADPKvcpEw-rFcg7yjtSgn54fGJUD94mS-AVWW5o",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NzY4Njk4LCJpYXQiOjE3Mjk3NjgzOTgsImp0aSI6ImEzZjQ3MDg5YzQ3MjQxNWRiMjEwOGM3ZTUwNmJjYmM2IiwidXNlcl9pZCI6NH0.nNWCxAS9-eCK-ZA7tXrTok38WWwisE5YFT-oLp-qkTM"
}
```

### 1. access token

It is used for client to authenticate the api calls, it expires after five minutes in simple jwt.
we can specify the time which after the access token expires.

but always, keep it short.

```py
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=5)
}
```

when access token expires, the `api` calls can no longer be authenticated with this access token.

<figure>
<img src="./assets/jwt.png" alt="jwt token" height="105" width="720" />
</figure>

### 2. refresh token

refresh token is used to regenerate the access token.
when access token expires after five minutes, it does not mean the user will be logout and have to login again. refresh token from previous call can be used to generate access token again. it is a security measure involved with `JWT`.

if we don't want someone to use the refresh token, we can black list them.

Now, in insomnia, with a valid user, generate a jwt with this
