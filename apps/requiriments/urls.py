from django.urls import path
from .views import *

urlpatterns = [
    path('requiriments/', requiriments, name='requiriments'),
]