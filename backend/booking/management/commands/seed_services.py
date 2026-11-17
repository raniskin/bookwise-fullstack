from django.core.management.base import BaseCommand
from booking.models import Service
class Command(BaseCommand):
 help='Create demo services'
 def handle(self,*args,**kwargs):
  for name,description,duration,price in [('Стрижка','Стрижка и укладка',60,1600),('Борода','Оформление бороды',30,900),('Комплекс','Стрижка + оформление бороды',90,2300)]:
   Service.objects.update_or_create(name=name,defaults={'description':description,'duration_minutes':duration,'price':price})
  self.stdout.write(self.style.SUCCESS('Demo services created'))
