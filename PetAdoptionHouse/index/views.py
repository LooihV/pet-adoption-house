from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse(f"Log in")

def catalogue(request):
    return HttpResponse(f"Catalogue")

def petmain(request):
    return HttpResponse(f"Pet #")

def adoption(request):
    return HttpResponse(f"Adoption")

