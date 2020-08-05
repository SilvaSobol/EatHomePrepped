from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from datetime import datetime
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # PASS tests whether a field matches the pattern            
            errors.append ("Invalid email address!")

        if len(postData['first_name']) < 2:
            errors.append("First name should be at least 2 characters long ")

        if len(postData['last_name']) < 2:
            errors.append("Last name should be at least 2 characters long ")

        if len(postData['email']) < 1:    #pass email cant be blank 
            errors.append("Invalid Email")
        
        if len(postData['psw']) < 8:  
           errors.append("Your password needs to be at least 8 characters long")
        
        if postData['psw'] != postData['confirm']:      #PASS if password does not match 
            errors.append("Password does not match!")

        result = User.objects.filter(email = postData['email']) #PASS if the email already exists!
        if result:
            errors.append("Email already created!")



       

class productManager(models.Manager):
    def basic_validator(self, postData):
        errors = []

        if len(postData['desc']) < 5:
            errors.append(" Description should be at least 5 characters long ")

        return errors



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    addess = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Product(models.Model):
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    desc = models.TextField(max_length=450)
    price =  price = models.DecimalField(decimal_places=2, max_digits=10)
    purchased_by = models.ManyToManyField(User, related_name ="has_bought") # users who bought specific product
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = productManager()

# class Order(models.Model):
#     total_price = models.DecimalField(decimal_places=2, max_digits=6)
#     placed_by = models.ForeignKey(User, related_name= "has_order", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


