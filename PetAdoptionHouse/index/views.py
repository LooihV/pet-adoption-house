from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, AdoptionForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import IdentificationType, Pet, Adoption, Event
from .models import User as UserCustom
from django.shortcuts import get_object_or_404
from datetime import date
import logging


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
                    return redirect('catalogue')
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


logger = logging.getLogger(__name__)


def request_adoption(request, pet_id):
    if request.user.is_authenticated:
        pet = get_object_or_404(Pet, id=pet_id, available=True)
        
        if request.method == 'POST':
            form = AdoptionForm(request.POST)
            if form.is_valid():
                adoption = form.save(commit=False)
                adoption.user = request.user
                adoption.pet = pet
                adoption.save()
                return render(request, 'index/adoption_result.html', {'adoption': adoption, 'success': True})
        else:
            form = AdoptionForm(initial={'pet': pet})

        return render(request, 'index/request_adoption.html', {'form': form, 'pet': pet})
    else:
        return redirect('login')


def adoptions(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            adoptions = Adoption.objects.all()

            if request.method == 'POST':
                adoption_id = request.POST.get('adoption_id')
                action = request.POST.get('action')

                if action in ['accept', 'decline']:
                    adoption = get_object_or_404(Adoption, id=adoption_id)
                    
                    print(f"Adoption ID: {adoption.id}, Action: {action}, Status: {adoption.status.id}")
                    
                    if action == 'accept':
                        adoption.status = Event.objects.get(id=2)
                        adoption.pet.available = False
                        adoption.pet.save()
                    elif action == 'decline':
                        adoption.status = Event.objects.get(id=3)

                    adoption.save()
        else:
            adoptions = Adoption.objects.filter(user=request.user)

        return render(request, 'index/adoptions.html', {'adoptions': adoptions})
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'index/profile.html', {'user': user})
    else:
        return redirect('login')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return render(request, 'index/logout.html')

