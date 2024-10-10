from django.contrib import admin
from .models import Train,Station,Passenger
# Register your models here.
class TrainAdmin(admin.ModelAdmin):
    list_display = ('TrainNo','org','desti','arrv_time','depart_time')

class StationAdmin(admin.ModelAdmin):
    list_display = ('code','city')
    
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('fisrt','last')
    filter_horizontal = ["trains_rev",]

admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Passenger, PassengerAdmin)
