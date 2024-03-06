from django.db import models

# Create your models here.
class Booking_Table(models.Model):
    name = models.CharField(max_length=200)
    Id = models.IntegerField()
    No_of_Guests = models.IntegerField()
    BookingDate = models.DateField()


def __str__(self):
    return self.name

class Menu_Table(models.Model):
    Id = models.IntegerField()
    Title= models.CharField(max_length=200)
    Price= models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

