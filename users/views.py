from django.shortcuts import render, redirect
from .models import Employee
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .utils import search_employees
# Create your views here.


@login_required(login_url="login")
@permission_required("users.view_users")
def profiles(response):

    employees, search_query = search_employees(response)
    user = response.user
    user = Employee.objects.get(user=user)
    context = {"employees": employees, "employee": user}
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
            return redirect('documents')
        else:
            messages.error(response, "Password or username is incorrect")
    try:
        user = response.user
        employee = Employee.objects.get(user=user)
    except:
        employee=None
    context = {"employee": employee, "page": page}
    return render(response, "users/login_registration_form.html", context)


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
            return redirect(response, "documents")
    user = response.user
    employee = Employee.objects.get(user=user)
    context = {"form": form, "employee": employee, "page": page}

    return render(response, "users/login_registration_form.html", context)


@login_required(login_url="login")
def logout_user(response):
    logout(response)
    redirect("login")
    messages.success(response, "User was successfully logged out")
    return redirect("login")


