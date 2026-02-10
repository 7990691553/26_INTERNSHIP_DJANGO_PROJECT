from django.contrib import admin
from .models import User, Visitor, Delivery, ChildAgeLimit, Child, StaffAttendance

# Register your models here.
admin.site.register(User)
admin.site.register(Visitor)
admin.site.register(Delivery)
admin.site.register(ChildAgeLimit)
admin.site.register(Child)
admin.site.register(StaffAttendance)
