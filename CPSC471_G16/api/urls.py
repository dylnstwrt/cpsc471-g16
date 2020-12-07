from django.urls import path, include
from . import views

urlpatterns = [
    path('employees', views.EmployeeList.as_view())
]
