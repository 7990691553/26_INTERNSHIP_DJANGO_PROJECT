from django.urls import path
from . import views

urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
]