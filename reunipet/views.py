from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib import messages

from reunipet.forms import SignUpForm

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