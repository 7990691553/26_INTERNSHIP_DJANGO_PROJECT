from django.urls import path
from . import views

urlpatterns = [
    path('serviceList/', views.serviceList,name="serviceList"),
    path('createService/',views.createService,name="createService"),
    path("deleteService/<int:id>",views.deleteService,name="deleteService"),
    path("updateService/<int:id>",views.updateService,name="updateService")
]