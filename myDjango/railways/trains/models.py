from django.db import models

# Create your models here.
class Station(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f'{self.code}:{self.city}'

class Train(models.Model):
    TrainNo = models.IntegerField()
    TrainName = models.CharField(max_length=30)
    org = models.ForeignKey(Station, on_delete=models.CASCADE,related_name='departures')
    desti = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arrivals')
    arrv_time = models.CharField(max_length=10)
    depart_time = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f'{self.org} to {self.desti} Arrv:{self.arrv_time} Depart:{self.depart_time}'
    
class Passenger(models.Model):
    fisrt = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    trains_rev = models.ManyToManyField(Train, blank=True, related_name='passengers')
    def __str__(self) -> str:
        return f'{self.fisrt} {self.last}'

    