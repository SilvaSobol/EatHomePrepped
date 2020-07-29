from django.shortcuts import render, redirect
from django.contrib.messages import error
from django.db import models
from django.contrib import messages
from .models import *


def index(request):
    return render (request, 'index.html')
