from django.contrib import admin
from django.urls import path, include

from Web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('smart_hand/', include('smart_hand.urls')),
    path('', views.auth, name='auth'),
]
