from django.shortcuts import render, redirect
from .models import Employee
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="login")
def profiles(response):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(response, "users/profiles.html", context)


@login_required(login_url="login")
def profile(response, pk):
    employee = Employee.objects.get(id=pk)
    context = {"employee": employee}
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
            messages.success(response, "User was successfully logged in")
            redirect("documents")
        else:
            messages.error(response, "Password or username is incorrect")

    context = {"page": page}
    return render(response, "users/login_register_form.html", context)


@login_required(login_url="login")
def register_user(response):
    page = "register"
    form = CustomUserCreationForm()
    if response.method == "POST":
        form = CustomUserCreationForm(response.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(response, user)
            redirect(response, "documents")
    context = {"form": form, "page": page}
    return render(response, "users/login_register_form.html", context)


@login_required(login_url="login")
def logout_user(response):
    logout(response)
    redirect("login")
    messages.success(response, "User was successfully logged out")
    return redirect("login")


def Account():
    pass
def editAccount():
    pass