import os
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def requiriments(request):
    


    return render(request, 'requiriments/requiriments.html')

def getImages(request):
    base_dir = '/home/jgonzalez/imagenesTAV'
    folders = []
    images = []

    for root, dirs, files in os.walk(base_dir):
        for name in dirs:
            folders.append(name)
        for name in files:
            if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, name))

    data = {
        'folders': folders,
        'images': images,
    }
    return JsonResponse(data)


def getImagesPath(request):
    base_dir = '/home/jgonzalez/imagenesTAV/'+request.GET.get('folder')
    images = []

    for root, dirs, files in os.walk(base_dir):
        for name in dirs:
            folders.append(name)
        for name in files:
            if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, name))

    data = {
        'folders': folders,
        'images': images,
    }
    return JsonResponse(data)
