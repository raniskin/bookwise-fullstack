from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Service,Appointment
from .serializers import ServiceSerializer,AppointmentSerializer
class ServicesView(APIView):
 def get(self,request):return Response(ServiceSerializer(Service.objects.all().order_by('id'),many=True).data)
class AppointmentsView(APIView):
 def post(self,request):
  # SQLite demo: transaction works for sequential requests; production needs row locks/constraints for concurrent slots.
  with transaction.atomic():
   s=AppointmentSerializer(data=request.data)
   s.is_valid(raise_exception=True)
   obj=s.save()
   return Response(AppointmentSerializer(obj).data,status=status.HTTP_201_CREATED)
