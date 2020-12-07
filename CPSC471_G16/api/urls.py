from django.urls import path, include
from . import views

urlpatterns = [
    path('employees', views.EmployeeList.as_view()),
    path('managers', views.ManagerList.as_view()),
    path('administrators', views.AdministratorList.as_view())
]

