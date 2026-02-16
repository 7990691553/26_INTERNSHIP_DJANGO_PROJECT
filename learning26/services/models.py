from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "SERVICES"

    def __str__(self):
        return self.name
