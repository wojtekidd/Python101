from django.db import models


# Create your models here.
class Flights(models.Model):
    origin = models.CharField(max_length=64, null=False)
    destination = models.CharField(max_length=64, null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.id}: from {self.origin} to {self.destination} - lasts {self.duration} minutes"

class Passengers(models.Model):
    name = models.CharField(max_length=64, null=False)
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)

