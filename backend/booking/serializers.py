from rest_framework import serializers
from .models import Service,Appointment
from django.utils import timezone
from datetime import timedelta
class ServiceSerializer(serializers.ModelSerializer):
 class Meta:
  model=Service
  fields=['id','name','description','duration_minutes','price']
class AppointmentSerializer(serializers.ModelSerializer):
 service_name=serializers.CharField(source='service.name',read_only=True)
 class Meta:
  model=Appointment
  fields=['id','service','service_name','customer_name','customer_email','starts_at','status']
  read_only_fields=['status']
 def validate(self,attrs):
  service=attrs['service'];start=attrs['starts_at'];end=start+timedelta(minutes=service.duration_minutes)
  if start<=timezone.now():raise serializers.ValidationError('Выберите время в будущем.')
  if start.minute not in (0,30):raise serializers.ValidationError('Начало записи — каждые 30 минут.')
  if not (9<=timezone.localtime(start).hour<20):raise serializers.ValidationError('Запись доступна с 09:00 до 20:00.')
  existing=Appointment.objects.filter(status='confirmed').select_related('service')
  for booking in existing:
   other_end=booking.starts_at+timedelta(minutes=booking.service.duration_minutes)
   if start<other_end and end>booking.starts_at:
    raise serializers.ValidationError('Это время уже занято. Выберите другой слот.')
  return attrs
