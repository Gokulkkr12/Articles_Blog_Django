# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect

def signup_details(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
            #login through redirect
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_details(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))


            else:
                return redirect('articles:list')



    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_details(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
