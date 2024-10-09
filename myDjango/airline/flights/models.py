from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.code} {self.city}'
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.origin} to {self.destination} : {self.duration}'

class Passenger(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')
    def __str__(self):
        return f'{self.first} {self.last}'