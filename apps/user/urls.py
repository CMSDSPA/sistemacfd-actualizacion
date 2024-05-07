from django.urls import path
from .views import index, home, custom_logout

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('logout/', custom_logout, name='logout'),
]