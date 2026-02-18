from django.db import models

# Create your models here.


# ===============================
# 1️⃣ Service Category Model
# ===============================

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


# ===============================
# 2️⃣ Service Provider Model
# ===============================

class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    experience_years = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name


# ===============================
# 3️⃣ Service Model (Main Model)
# ===============================

class Service(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services"
    )
    providers = models.ManyToManyField(
        ServiceProvider,
        related_name="provided_services",
        blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


# ===============================
# 4️⃣ Customer Model
# ===============================

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


# ===============================
# 5️⃣ Booking Model
# ===============================

class Booking(models.Model):

    BOOKING_STATUS = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    provider = models.ForeignKey(
        ServiceProvider,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings"
    )

    booking_date = models.DateTimeField(auto_now_add=True)
    service_date = models.DateField()
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='Pending')

    def __str__(self):
        return f"{self.customer.name} - {self.service.name}"


# ===============================
# 6️⃣ Payment Model
# ===============================

class Payment(models.Model):

    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
        ('Net Banking', 'Net Banking'),
    ]

    PAYMENT_STATUS = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    ]

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Unpaid')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id}"


# ===============================
# 7️⃣ Review Model
# ===============================

class Review(models.Model):

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.service.name}"
