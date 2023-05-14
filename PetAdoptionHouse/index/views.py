from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "index/login.html")

def home(request):
    return HttpResponse(f"Home!!!")

def catalogue(request):
    return HttpResponse(f"Catalogue")

def petmain(request):
    return HttpResponse(f"Pet #")

def adoption(request):
    return HttpResponse(f"Adoption")

