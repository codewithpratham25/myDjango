from datetime import datetime, date
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, 'newyear/index.html',{
        'newyear': now.month == 1 and now.day == 1
    })
def days(request):
    now = date.today()
    n_date = date(2025,1,1)
    delta = n_date - now
    days_left = delta.days
    return render(request,'newyear/index.html',{
        'delta': days_left
    })