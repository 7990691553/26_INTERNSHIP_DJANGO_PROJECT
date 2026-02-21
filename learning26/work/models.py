from django.db import models

# Create your models here.
# Below classes/models are my actual project models of eSociety, which will be used to create tables in the database in upcoming sessions.

class User(models.Model):
    ROLE_CHOICES = (
        ("SUPER_ADMIN", "Super Admin"),
        ("ADMIN", "Admin / Chairman"),
        ("MEMBER", "Society Member"),
        ("SECURITY", "Security Person"),
        ("HELPER", "House Helper"),
    )

    userName = models.CharField(max_length=30)
    userRole = models.CharField(max_length=15, choices=ROLE_CHOICES)
    flatNo = models.CharField(max_length=10)
    contactNo = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.userName

class Visitor(models.Model):
    VISITOR_TYPE = (
        ("GUEST", "Guest"),
        ("SERVICE", "Service Provider"),
    )

    APPROVAL_STATUS = (
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    visitorName = models.CharField(max_length=30)
    visitorType = models.CharField(max_length=15, choices=VISITOR_TYPE)
    visitPurpose = models.CharField(max_length=100, null=True, blank=True)  # NEW FIELD
    priorPermission = models.BooleanField(default=False)
    approvalStatus = models.CharField(max_length=10, choices=APPROVAL_STATUS, default="PENDING")

    memberId = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)  # NEW

    class Meta:
        db_table = "visitor"

    def __str__(self):
        return self.visitorName
    
class VisitorEntryLog(models.Model):
    visitorId = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    entryTime = models.DateTimeField()
    exitTime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "visitor_entry_log"

    def __str__(self):
        return self.visitorId.visitorName



class Delivery(models.Model):
    DELIVERY_STATUS = (
        ("PENDING", "Pending"),
        ("COLLECTED", "Collected"),
    )

    deliveryPerson = models.CharField(max_length=30)
    deliveryAllowed = models.BooleanField()
    deliveryStatus = models.CharField(max_length=10, choices=DELIVERY_STATUS)
    storedAtSecurity = models.BooleanField()

    memberId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "delivery"

    def __str__(self):
        return self.deliveryPerson
    
class DeliveryLog(models.Model):
    deliveryId = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    receivedTime = models.DateTimeField()
    collectedTime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "delivery_log"

    def __str__(self):
        return self.deliveryId.deliveryPerson



class ChildAgeLimit(models.Model):
    ageLimit = models.IntegerField()

    class Meta:
        db_table = "child_age_limit"

    def __str__(self):
        return str(self.ageLimit)


class Child(models.Model):
    childName = models.CharField(max_length=30)
    childAge = models.IntegerField()
    childPhoto = models.FileField(upload_to="child_photos/", null=True, blank=True)  # NEW
    inTime = models.TimeField()
    outTime = models.TimeField()

    parentId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "child"

    def __str__(self):
        return self.childName


class StaffAttendance(models.Model):
    STAFF_ROLE = (
        ("SECURITY", "Security"),
        ("HELPER", "House Helper"),
    )

    staffName = models.CharField(max_length=30)
    staffRole = models.CharField(max_length=20, choices=STAFF_ROLE)
    attendanceDate = models.DateField()
    staffInTime = models.TimeField()
    staffOutTime = models.TimeField()

    class Meta:
        db_table = "staff_attendance"

    def __str__(self):
        return self.staffName

class SocietyNotice(models.Model):
    noticeTitle = models.CharField(max_length=100)
    noticeDescription = models.TextField()
    postedDate = models.DateField()
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "society_notice"

    def __str__(self):
        return self.noticeTitle

class SocietySettings(models.Model):
    deliveryAllowed = models.BooleanField(default=True)
    visitorAllowed = models.BooleanField(default=True)
    defaultAgeLimit = models.IntegerField(default=3)

    class Meta:
        db_table = "society_settings"

    def __str__(self):
        return "Society Settings"