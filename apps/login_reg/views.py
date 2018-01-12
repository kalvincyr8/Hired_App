from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib import messages
import datetime

def index(request):
    return render(request, "login_reg/index.html")

def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.error(request, 'User has been created')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        print 'failed to login'
        messages.error(request, 'Please check your Email and Password and try again')
        return redirect('/')
    request.session['email'] = results['user'].email
    print "created user"
    request.session['first_name'] = results['user'].first_name
    request.session['user_id'] = results['user'].id

    return redirect("/index")


def logout(request):
    request.session.flush()
    return redirect('/')
