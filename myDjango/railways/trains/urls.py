from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:TrainNo>', views.train, name='train'),
    path('stations/', views.station, name='station'),
    path('<int:TainNo>/book', views.book, name='book')
]


