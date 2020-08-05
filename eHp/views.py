from django.shortcuts import render, redirect
from django.contrib.messages import error
from django.db import models
from django.contrib import messages
from .models import *


def index(request):
    return render (request, 'index.html')

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def item_menu(request):
    context = {}
    return render(request, 'menu.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)
    
def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    
    if errors:
        for e in errors:
            error(request, e)
        return redirect('/')
    else:
        user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'],password=request.POST['password'])
        request.session['userID'] = user.id 
        request.session['name'] = user.first_name
        return redirect('/dashboard')

def user_login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            request.session['userID'] = logged_user.id 
            request.session['name'] = logged_user.first_name 
            return redirect('/dashboard')
        elif logged_user.password != request.POST['password']:
            error(request, "Incorrect password")
        return redirect ('/')
    else:
        error(request, "This email has not been registered.")
        return redirect('/')
