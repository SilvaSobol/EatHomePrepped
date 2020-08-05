from django.shortcuts import render, redirect
from django.contrib.messages import error
from django.db import models
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render (request, 'index.html')

def cart(request):
    context = {
        'user': User.objects.get(id = request.session['userid']),
    }
    return render(request, 'cart.html', context)

def item_menu(request):
    context = {}
    return render(request, 'menu.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)


def create_user(request): #PASS
    # pass the post data to the method we wrote and save the response in a variable called errors
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if errors:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for e in errors:
                error(request, e)
        # redirect the user back to the form to fix the errors
            return redirect('/')
        # if the errors object is empty, that means there were no errors!

        else:  #PASS THIS HELPS HASH THE PASSWORD
            hashed_pw = bcrypt.hashpw(request.POST['psw'].encode(),bcrypt.gensalt()).decode()   # ADD DECODE METHOD TO THE END
            user = User.objects.create( 
                first_name = request.POST['first_name'], 
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = hashed_pw,
            )
            request.session['userid']=user.id

        return redirect('/cart')
    

def user_login(request): #PASS 
    email = User.objects.filter(email=request.POST['email'])

    if len(email) > 0:
        logged_user = email[0]

        if bcrypt.checkpw(request.POST['psw'].encode(),logged_user.password.encode()): # COMPARES THE EXISTED PSW MATCH
            request.session['userid'] = logged_user.id
            return redirect('/cart')
        else:
           messages.error(request,"Email and Password did not match")
    else:
        messages.error(request,"This email has not been registered yet!")
    return redirect('/')


def log_out(request):
    request.session.clear()    #pass delete the current session    
    return render(request, "index.html")

