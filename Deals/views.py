from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
# Create your views here.
def signup(request):
    if request.method=="GET":
        return render(request,'Deals/signup.html',{'form':UserCreationForm})
    else:
        if request.POST(['password1'])==request.POST(['password2']):
