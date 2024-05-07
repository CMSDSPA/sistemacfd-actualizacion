
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'user/index.html')

@login_required
def home(request):
    if request.user.is_authenticated:
        template = 'user/home.html'
        return render(request, template)
    else:
        return redirect('index')

def custom_logout(request):
    logout(request)
    return redirect('index')

