from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout
# Create your views here.
def signup(request):
    if request.method=="GET":
        return render(request,'Deals/signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current')
            except IntegrityError:
                return render(request,'Deals/signup.html',{'form':UserCreationForm,"error":"User had been registered"})
        else:
            return render(request,'Deals/signup.html',{'form':UserCreationForm,"error":"Password do not repeated"})
def current(request):
    return render(request,'Deals/current.html')
def logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')
def home(request):
    return render(request,'Deals/home.html')