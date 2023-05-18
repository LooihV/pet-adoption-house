from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import IdentificationType, Pet



def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalogue'))
    else:    
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            try:   
                if form.is_valid():
                    email = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('catalogue')
            except Exception as e:
                erorr_message = "Error: "+str(e)
                return render(request, 'index/login.html', {'form':form, 'error_message': erorr_message})
        else:
            form = AuthenticationForm()        
        return render(request, "index/login.html", {'form':form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalogue'))
    else:          
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            try:
                if form.is_valid():
                    user_profile = form.save()
                    login(request, user_profile)
                    return redirect('home')
            except Exception as e:
                erorr_message = "Error: "+str(e)
                return render(request, 'index/login.html', {'form':form, 'error_message': erorr_message})
        else:
            form = RegistrationForm()
        idtypes = IdentificationType.objects.all()        
        return render(request, "index/register.html", {'form':form, 'identification_type':idtypes})
                

def catalogue(request):
    pets = Pet.objects.all()
    return render(request, "index/catalogue.html", {'pets':pets})

def pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'index/pet_detail.html', {'pet': pet})

def adoption(request):
    return HttpResponse(f"Adoption")

def account(request):
    return HttpResponse(f"Account! xd")

