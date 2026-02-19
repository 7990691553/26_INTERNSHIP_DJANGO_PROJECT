from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Booking, ServiceCategory, ServiceProvider, Customer, Payment, Review
from .forms import ServiceForm, BookingForm
from django.db.models import Q, Avg 


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
    query = request.GET.get('q')

    if query:
        services = Service.objects.filter(
            Q(name__icontains=query)
        )
    else:
        services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'services/service_list.html', context)


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

def home(request):
    services = Service.objects.filter(status='Active')[:6]
    return render(request, 'services/home.html', {
        'services': services
    })


def category_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'services/category_list.html', {
        'categories': categories
    })


def services_by_category(request, pk):
    category = get_object_or_404(ServiceCategory, id=pk)
    services = category.services.filter(status='Active')

    return render(request, 'services/services_by_category.html', {
        'category': category,
        'services': services
    })

def service_detail(request, pk):
    service = get_object_or_404(Service, id=pk)
    return render(request, 'services/service_detail.html', {
        'service': service
    })

