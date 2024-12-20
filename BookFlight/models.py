from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=15, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=75)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} ({self.origin} to {self.destination})"

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight, related_name="passengers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"