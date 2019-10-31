from django.shortcuts import render, redirect
from polls.models import DustBin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    current_plastic_level = DustBin.objects.filter(type=DustBin.PLASTIC).last().level
    current_metal_level = DustBin.objects.filter(type=DustBin.METAL).last().level
    current_other_level = DustBin.objects.filter(type=DustBin.OTHERS).last().level


    return render(request, 'dashboard.html', {
        "current_plastic_level":current_plastic_level,
        "current_metal_level":current_metal_level,
        "current_other_level":current_other_level})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    return render(request, 'register.html', {'form': form})   

def layout(request):
    return render(request, 'layout.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def logout(request):
    return render(request, 'logout')