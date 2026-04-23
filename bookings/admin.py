from django.contrib import admin
from .models import Ambulance, Booking

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate_number', 'status')
    list_filter = ('status',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'ambulance', 'emergency_level', 'created_at')
    list_filter = ('emergency_level',)