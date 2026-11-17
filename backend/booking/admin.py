from django.contrib import admin
from .models import Service,Appointment
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
 list_display=['name','duration_minutes','price']
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
 list_display=['customer_name','service','starts_at','status']
 list_filter=['status','service']
 search_fields=['customer_name','customer_email']
