from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/user/', include('rest_auth.urls')),
    path('api/user/registration/', include('rest_auth.registration.urls')),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
