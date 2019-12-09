import json
from django.shortcuts import render, redirect
from polls.models import DustBin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    def get_last_entry(type_):
        if DustBin.objects.filter(type=type_).count() > 0:
            return DustBin.objects.filter(type=DustBin.PLASTIC).last().level
        return 0

    if not request.user.is_authenticated:
        return redirect('login')
    current_plastic_level = get_last_entry(DustBin.PLASTIC)
    current_metal_level = get_last_entry(DustBin.METAL)
    current_other_level = get_last_entry(DustBin.OTHERS)
    metal_data = list(reversed(DustBin.objects.filter(type=DustBin.METAL).order_by('-id').values_list('level', flat=True)[:7]))
    plastic_data = list(reversed(DustBin.objects.filter(type=DustBin.PLASTIC).order_by('-id').values_list('level', flat=True)[:7]))
    other_data = list(reversed(DustBin.objects.filter(type=DustBin.OTHERS).order_by('-id').values_list('level', flat=True)[:7]))

    return render(request, 'dashboard.html', {
        "current_plastic_level":current_plastic_level,
        "current_metal_level":current_metal_level,
        "current_other_level":current_other_level,
        "plastic_data": json.dumps(plastic_data),
        "metal_data": json.dumps(metal_data),
        "other_data": json.dumps(other_data),
        })

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

# # def login(request):
# #     return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

# def logout(request):
#     return render(request, 'logout')