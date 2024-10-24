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
    path("api/token/",TokenObtainPairView.as_view(), name="token_obtain_pair_review"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh_view")
]
# Debug toolbar URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

