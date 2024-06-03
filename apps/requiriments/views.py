from django.shortcuts import render

# Create your views here.
def requiriments(request):
    return render(request, 'requiriments/requiriments.html')
