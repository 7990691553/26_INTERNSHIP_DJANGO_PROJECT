from django.shortcuts import render
from .models import Visitor, Delivery, Child, StaffAttendance
from django.utils.timezone import now

# Create your views here.

def dashboard(request):
    today = now().date()

    visitor_count = Visitor.objects.count()
    delivery_count = Delivery.objects.count()
    child_count = Child.objects.count()
    staff_today = StaffAttendance.objects.filter(attendanceDate=today).count()

    context = {
        "visitor_count": visitor_count,
        "delivery_count": delivery_count,
        "child_count": child_count,
        "staff_today": staff_today
    }

    return render(request, "work/dashboard.html", context)
