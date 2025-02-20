from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("knowledgebot_home")
    else:
        form = UserCreationForm()
    return render(request, "knowledgebot/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("knowledgebot_home")
        else:
            return render(request, "knowledgebot/login.html", {"error": "Invalid credentials"})
    return render(request, "knowledgebot/login.html")

@login_required
def knowledgebot_home(request):
    return render(request, "knowledgebot/home.html")

def logout_view(request):
    logout(request)
    return redirect("login")
