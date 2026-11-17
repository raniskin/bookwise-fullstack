from django.urls import path
from .views import ServicesView,AppointmentsView
urlpatterns=[path('services/',ServicesView.as_view()),path('appointments/',AppointmentsView.as_view())]
