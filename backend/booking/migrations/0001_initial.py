from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[migrations.CreateModel(name='Service',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=100)),('description',models.CharField(blank=True,max_length=220)),('duration_minutes',models.PositiveIntegerField(default=60)),('price',models.PositiveIntegerField(default=1000))]),migrations.CreateModel(name='Appointment',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('customer_name',models.CharField(max_length=120)),('customer_email',models.EmailField(max_length=254)),('starts_at',models.DateTimeField()),('status',models.CharField(choices=[('confirmed','Подтверждено'),('cancelled','Отменено')],default='confirmed',max_length=12)),('created_at',models.DateTimeField(auto_now_add=True)),('service',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='appointments',to='booking.service'))],options={'ordering':['starts_at']})]
