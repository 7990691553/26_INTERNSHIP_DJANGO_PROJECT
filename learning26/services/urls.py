from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
   # Public pages
    path('lol/', views.home, name="home"),
    path('categories/', views.category_list, name="category_list"),
    path('category/<int:pk>/', views.services_by_category, name="services_by_category"),
    path('service/<int:pk>/', views.service_detail, name="service_detail"),

    # Dashboard (Admin)
    path('dashboard/', views.dashboard, name="dashboard"),
    path('services/', views.service_list, name="service_list"),
    path('services/create/', views.create_service, name="create_service"),
    path('bookings/', views.booking_list, name="booking_list"),
    path('bookings/create/', views.create_booking, name="create_booking"),
]
