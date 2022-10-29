from django.shortcuts import render
# Create your views here.
def signup(request):
    if request.method=="GET":
        return render(request,'Deals/signup.html')
    else:
        pass