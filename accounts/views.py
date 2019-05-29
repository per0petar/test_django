# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, RegisterForm, UpdateUserFrom



# Create your views here.

def login_view(request, *args):
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")        
    else:
        form = UserLoginForm()

    return render(request, "login.html", context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "sign_up.html", context)

def logout_view(request):
    logout(request)
    return render(request, "logout.html", {})

@login_required
def update_view(request):
    
    u_form = UpdateUserFrom(instance=request.user)
    context = {
        "form"    : u_form
    }  
    if request.method == 'POST':
        u_form = UpdateUserFrom(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            username = u_form.cleaned_data.get("username")
            password = u_form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "pages/profile_home.html", context)
    else:
        u_form = UpdateUserFrom(instance=request.user)
    return render(request, "pages/profile_update.html", context)