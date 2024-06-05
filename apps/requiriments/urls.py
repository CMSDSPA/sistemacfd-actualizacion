from django.urls import path
from .views import *

urlpatterns = [
    path('requiriments/', requiriments, name='requiriments'),
    path('getImages/', getImages, name='getImages'),
    path('getImagesPath/', getImagesPath, name='getImagesPath'),
    # path('serve-image/<path:image_path>/', views.serve_image, name='serve_image'),


]