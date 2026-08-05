from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150,required=True)
    last_name = forms.CharField(max_length=150, required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

CHOICES = {"ALA": "Alajuela", "CAR": "Cartago", "GUA": "Guanacaste", "HER": "Heredia", "LIM": "Limón", "PUN": "Puntarenas", "SAN": "San José"}
class LostPetForm(forms.Form):
    pet_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    province = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    reward_for_information = forms.BooleanField(required=False)
    last_time_been_seen_at = forms.CharField(max_length=100)
    
