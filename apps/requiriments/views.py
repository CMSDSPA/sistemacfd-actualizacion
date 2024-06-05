import os
from django.http import FileResponse, Http404, JsonResponse
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
    base_dir = '/home/jgonzalez/imagenesTAV/'+request.GET.get('folder')+'/'
    print(base_dir)
    images = []

    for root, dirs, files in os.walk(base_dir):
        for name in files:
            if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, name))

    data = {
        'images': images,
    }
    return JsonResponse(data)


def serve_image(request, image_path):
    image_path_full = os.path.join('/home/jgonzalez/imagenesTAV/', image_path)
    if os.path.exists(image_path_full):
        return FileResponse(open(image_path_full, 'rb'))
    else:
        raise Http404("Image not found")