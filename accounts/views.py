from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            password = request.POST.get('password')
            email = request.POST.get('email')

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")	
                return redirect('dashboard')
            else:
                messages.error(request, "Please enter a valid email and password.")
    return render(request, 'dashboard/login.html', {})

def logout_view(request):
	logout(request)
	return redirect('login')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.UserFormCreate(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password1)
                if user is not None:
                    if request.user.is_authenticated:
                        logout(request)
                    login(request, user)
                messages.success(request, f"User was successfully created. Please log in. ")
                return redirect('dashboard')
				
            messages.error(request, f"Unable to create account")
        else:
            form = forms.UserFormCreate()
    else:
        return redirect('dashboard') 


    context = {'form': form}
    return render(request, 'dashboard/signup.html', context=context)