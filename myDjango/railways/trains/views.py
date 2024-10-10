from django.shortcuts import render
from django.urls import reverse
from .models import Station,Train,Passenger
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'trains/index.html',{
        'trains':Train.objects.all()
    })
def train(request,TrainNo):
    train = Train.objects.get(pk=TrainNo)
    return render(request, 'trains/train.html',{
        'train':train,
        'passengers':train.passengers.all(),
        'non_passengers':Passenger.objects.exclude(trains_rev=train).all()
    })
    
def station(request):
    return render(request, 'trains/station.html',{
        'stations':Station.objects.all()
    })
def book(request, TrainNo):
    if request.method == 'POST':
        train = Train.objects.get(id=TrainNo)
        passenger = Passenger.objects.get(id=int(request.POST['passenger']))
        passenger.trains.add(train)
        return HttpResponseRedirect(reverse('train', args=(train.id,)))
        
        
