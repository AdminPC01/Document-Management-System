from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.messages import messages
# Create your views here.


def profiles(response):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(response, "users/profiles.html", context)


def profile(response, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(response, "users/profile.html", context)


def login_user(response):
    page = "login"
    if response.method == "POST":
        username = response.POST["username"]
        password = response.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(response, "Username doesn't exist")

        user = authenticate(response, username=username, password=password)

        if user is not None:
            login(response, user)
            redirect("documents")
            messages.success(response, "User was successfully logged in")
        else:
            messages.error(response, "Password or username is incorrect")

    context = {"page": login}
    return render(response, "login_register_form.html", context)


def register_user(response):
    form = CustomUserCreationForm()
    if response.method == "POST":
        form = CustomUserCreationForm(response.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(response, user)
            redirect(response, "documents")
    context = {}
    return render(response, "users/login_register_form.html", context)


@login_required(login_url="login")
def logout(response):
    user = response.user
    logout(response)
    redirect("login")
    messages.success(response, "User was successfully logged out")
