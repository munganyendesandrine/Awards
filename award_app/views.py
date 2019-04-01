from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):   
    return render(request,'welcome.html')