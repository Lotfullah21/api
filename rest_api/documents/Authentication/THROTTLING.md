# Throttling

an efficient technique to prevent API abuse, with throttling we can control how often an API can be accessed.
throttling classes are built within `DRF` and there are two major types of throttling.

### 1. Anonymous Throttling for Unauthenticated users

It will be used when there is no token in the API header

Let's create an end point and make some limitation for it's access.

```py
#views.py
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
@throttle_classes([AnonRateThrottle])
@api_view()
def throttle_check(request):
    return Response({"message": "From throttling"})
```

```py
#urls.py
from django.urls import path
from .views import throttle_check
urlpatterns = [
    path("throttle_check/",throttle_check,name="throttle_check_view"),
]

```

Now, in `settings.py` add the anonymous throttling rate.

```py
#settings.py

# Renderer
REST_FRAMEWORK = {
   'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
    },
}
```

Now, if the user is not authenticated, the throttling rate will be `2` request per minute.

### 2. User Throttling for Authenticated users

It will be used when there are valid tokens,

the steps are exactly the same as anonymous user, but with different classes and settings.

```py
# views.py
from rest_framework.throttling import UserRateThrottle
@api_view()
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def throttle_check_auth(request):
    return Response({"message": "From authenticated throttling"})
```

map the function to a URL

```py
from django.urls import path
from .views import Courses, secret, teachers_view, throttle_check,throttle_check_auth
urlpatterns = [
    path("throttle_check_auth/",throttle_check_auth,name="throttle_check_auth_view"),
]
```

```py
# settings.py
REST_FRAMEWORK = {
   'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user':'10/minute'
    },
}
```

With the above setup in our `settings.py`, all of our `API` end points will have a throttling rate for authenticated users and for anonymous user.

Now, what if we want to have different throttling for different views.

create a new file named `throttles.py` in the app directory.

this file creates a new throttle policy with the scoop name.

```py
# throttles.py
from rest_framework.throttling import UserRateThrottle
class FiveCallsPerMinute(UserRateThrottle):
    scope="five"
```

```py

# Renderer
REST_FRAMEWORK = {
   'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user':'10/minute',
        'five':"5/minute",
    },
}

```

Now import the policy in `views.py` and we can use the above throttling class for any of our authenticated user on different API end points.

```py
#views.py
from .throttles import FiveCallsPerMinute
@api_view()
@throttle_classes([FiveCallsPerMinute])
@permission_classes([IsAuthenticated])
def throttle_check_auth(request):
    return Response({"message": "From authenticated throttling"})
```

Now, user can make five requests to `throttle_check_auth`.

## Throttling for class based views

Class-based views don’t use the throttle_classes decorator like function-based views. To use throttling, you need to pass the throttle classes to a public class property called throttle_classes. First import the necessary classes in the views.py file.

```py
class Courses(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    MAX_PER_PAGE = 10
    def get(self, request):
        courses = Course.objects.all()
        pass
```
