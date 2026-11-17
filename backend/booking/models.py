from django.db import models
class Service(models.Model):
 name=models.CharField(max_length=100)
 description=models.CharField(max_length=220,blank=True)
 duration_minutes=models.PositiveIntegerField(default=60)
 price=models.PositiveIntegerField(default=1000)
 def __str__(self):return self.name
class Appointment(models.Model):
 STATUS_CHOICES=[('confirmed','Подтверждено'),('cancelled','Отменено')]
 service=models.ForeignKey(Service,on_delete=models.PROTECT,related_name='appointments')
 customer_name=models.CharField(max_length=120)
 customer_email=models.EmailField()
 starts_at=models.DateTimeField()
 status=models.CharField(max_length=12,choices=STATUS_CHOICES,default='confirmed')
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=['starts_at']
 def __str__(self):return f'{self.customer_name} — {self.starts_at}'
