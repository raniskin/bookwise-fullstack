from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Service
class BookingTests(TestCase):
 def setUp(self):self.service=Service.objects.create(name='Test',duration_minutes=60,price=1000)
 def test_services_endpoint(self):self.assertEqual(self.client.get('/api/services/').status_code,200)
 def test_appointment_requires_future(self):
  res=self.client.post('/api/appointments/',data={'service':self.service.pk,'customer_name':'User','customer_email':'user@example.com','starts_at':(timezone.now()-timedelta(days=1)).isoformat()},content_type='application/json')
  self.assertEqual(res.status_code,400)
