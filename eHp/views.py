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