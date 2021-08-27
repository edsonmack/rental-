from __future__ import unicode_literals
#from django.http import HttpResponse
from django.shortcuts import render,redirect
#from .models import Reconsiliation
#from django.db.models import Count
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.decorators import permission_required

# Create your views here.


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def change_password(request):
    return render(request, 'change_password.html')

def home(request):
    return render(request, 'home.html')
