# core/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')