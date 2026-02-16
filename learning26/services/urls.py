from django.urls import path
from . import views

urlpatterns = [
    path('serviceList/', views.serviceList,name="serviceList"),
    path('createService/',views.createService,name="createService")
]