from django.contrib import admin
from django.urls import path, include

from smart_hand import views

app_name = 'employee'

urlpatterns = [
    path('', views.show_application, name='application'),
    path('work_plan/<int:pk>/', views.show_work_plan_detail, name='work_plan_detail'),
]
