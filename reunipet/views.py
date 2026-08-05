from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from reunipet.forms import SignUpForm, LostPetForm
from .models import LostPet
# Create your views here.



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account was successfully created')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'reunipet/sign_up.html', {"form": form})

def about(request):
    return render(request, 'reunipet/about.html')

def index(request):
    return render(request, 'reunipet/index.html')

@login_required
def report(request):
    if request.method == "POST":
        form = LostPetForm(request.POST)
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        
        
        if form.is_valid() and latitude != "" and longitude != "":
            # Success code
            print(form.cleaned_data["pet_name"])
            print(form.cleaned_data["province"])
            print(form.cleaned_data["last_time_been_seen_at"])
            print(form.cleaned_data["reward_for_information"])
            lost_pet = LostPet(pet_name = form.cleaned_data["pet_name"], province = form.cleaned_data["province"], last_time_been_seen_at = form.cleaned_data["last_time_been_seen_at"], reward_for_information = form.cleaned_data["reward_for_information"], latitude = request.POST["latitude"], longitude = request.POST["longitude"] )
            lost_pet.save()
            return HttpResponseRedirect(reverse("reunipet:home"))
        else:
            if latitude == "" or longitude == "":
                return render(request, 'reunipet/report.html', {"form": form, "error_message":"You must pin point the closest location your pet was lost. JavaScrip must be enabled"})
            else:
                return render(request, "reunipet/report.html" ,{"form": form})
                
    else:
        form = LostPetForm()
    return render(request, 'reunipet/report.html', {"form": form})

def account_settings(request):
    return render(request, 'reunipet/account_settings.html')

def your_lost_pets_list_list(request):
    return render(request, 'reunipet/your_lost_pets_list.html')