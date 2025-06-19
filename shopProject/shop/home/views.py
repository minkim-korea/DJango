from django.shortcuts import render

def step01(request):
    return render(request, 'step01.html')

def index(request):
    return render(request, 'index.html')
