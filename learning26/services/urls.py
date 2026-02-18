from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('services/', views.service_list, name="service_list"),
    path('services/create/', views.create_service, name="create_service"),
    path('bookings/', views.booking_list, name="booking_list"),
    path('bookings/create/', views.create_booking, name="create_booking"),
]
