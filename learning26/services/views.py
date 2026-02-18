from django.shortcuts import render, redirect
from .models import Service, Booking
from .forms import ServiceForm, BookingForm


# Dashboard
def dashboard(request):
    total_services = Service.objects.count()
    total_bookings = Booking.objects.count()

    context = {
        'total_services': total_services,
        'total_bookings': total_bookings,
    }
    return render(request, "services/dashboard.html", context)


# Service List
def service_list(request):
    services = Service.objects.all()
    return render(request, "services/service_list.html", {'services': services})


# Create Service
def create_service(request):
    form = ServiceForm()
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services:service_list')
    return render(request, "services/service_form.html", {'form': form})


# Booking List
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "services/booking_list.html", {'bookings': bookings})


# Create Booking
def create_booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services:booking_list')
    return render(request, "services/booking_form.html", {'form': form})
