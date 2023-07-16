from django.contrib import admin

# Register your models here.
from .models import Measurement,Sensor

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass

@admin.register(Sensor)
class SemsorAdmin(admin.ModelAdmin):
    pass