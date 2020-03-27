from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'oceanapp/index.html')

def register(request):
    return render(request, 'oceanapp/register.html')

def dashboard(request):
    return render(request, 'oceanapp/dashboard.html')