from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def host(request):
    return render(request, 'admin.html')