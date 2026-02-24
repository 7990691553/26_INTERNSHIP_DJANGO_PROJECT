from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.utils.timezone import now

def dashboard(request):
    today = now().date()

    context = {
        "visitor_count": Visitor.objects.count(),
        "delivery_count": Delivery.objects.count(),
        "child_count": Child.objects.count(),
        "staff_today": StaffAttendance.objects.filter(attendanceDate=today).count(),
        "recent_visitors": Visitor.objects.order_by("-createdAt")[:5],
    }

    return render(request, "work/dashboard.html", context)


# ---------------- VISITOR ----------------


def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, "work/visitor_list.html", {"visitors": visitors})


def add_visitor(request):
    form = VisitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("visitor_list")
    return render(request, "work/visitor_form.html", {"form": form})


# ---------------- DELIVERY ----------------

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "work/delivery_list.html", {"deliveries": deliveries})


def add_delivery(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("delivery_list")
    return render(request, "work/delivery_form.html", {"form": form})


# ---------------- CHILD ----------------

def child_list(request):
    children = Child.objects.all()
    return render(request, "work/child_list.html", {"children": children})

def add_child(request):
    form = ChildForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("child_list")
    return render(request, "work/child_form.html", {"form": form})


# ---------------- STAFF ----------------

def staff_list(request):
    staff = StaffAttendance.objects.all()
    return render(request, "work/staff_list.html", {"staff": staff})

def add_staff(request):
    form = StaffAttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("staff_list")
    return render(request, "work/staff_form.html", {"form": form})


# ---------------- NOTICE ----------------

def notice_list(request):
    notices = SocietyNotice.objects.all()
    return render(request, "work/notice_list.html", {"notices": notices})

def add_notice(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("notice_list")
    return render(request, "work/notice_form.html", {"form": form})