from django.contrib import admin
from .models import *

admin.site.register(ServiceCategory)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)

