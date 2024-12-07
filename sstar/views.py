from django.shortcuts import render,redirect
from urllib3 import request

from .forms import DataForm, CreateAccount

from django.contrib import messages
from .models import TabHeader,Tab,Insurance

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms


def insurance(request, pk):
    insurance = Insurance.objects.get(id=pk)
    return render(request, 'insurance.html', {"insurance": insurance})

def home(request):
    return render(request, 'index.html')

def about(request):
    tabheaders = TabHeader.objects.all()
    tabs = Tab.objects.all()
    return render(request, 'about.html', {'tabheader': tabheaders, 'tab': tabs})

def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    insurance = Insurance.objects.all()
    return render(request, 'service-details.html', {"insurance": insurance})

def application(request):
    if request.method == 'POST':
        form = DataForm(request.POST or None, request.FILES)
        # incase form is valid

        if form.is_valid():
           form.save()
           messages.success(request, 'Your application has successfully been registered.')
           # clearing the form

           form = DataForm()
           return render(request, 'application.html', {'form': form})
        else:
            return render(request, 'application.html', {'form': form})

    else:
        form = DataForm()
        return render(request, 'application.html', {'form': form})

def register_user(request):
    form = CreateAccount()
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successfully, Login to continue")

            # redirect to Login Page
            return redirect('/')
        else:
            messages.success(request, "Ooops! there was an error creating your account")
            return redirect('register')
    else:
        return render (request, 'sign.html', {'form' :form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('/')
    else:
        messages.success(request, 'There is an error, please try again')
        return redirect('login')

    return render (request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out... Thanks for stopping by...')
    return redirect('/')
    pass
def contact(request):
    return render(request, 'contact.html')