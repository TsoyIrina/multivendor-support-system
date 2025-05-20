from django.contrib import admin
from django.urls import path, include

from client import views
app_name = 'client'

urlpatterns = [
    path('create_application/', views.create_application, name='create_application'),
    path('profile/', views.profile, name='profile'),
    path('dalete/<int:pk>/', views.delete_address, name='delete_address'),
    path('update/', views.update_profile, name='update_profile'),
    path('application', views.show_application, name='application'),
    path('work_plan/<int:pk>/', views.show_work_plan_detail, name='work_plan_detail'),
    path('agreed/<int:pk>/', views.agreed, name='agreed'),
]
