from django.contrib import admin
from django.urls import path, include
from drfsite.routers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',  include(router().urls)),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('api/drf-auth/', include('rest_framework.urls')),
]
