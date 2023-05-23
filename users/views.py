from django.shortcuts import render

# Create your views here.


def loginUser(response):
    context = {}
    return render(response,"login_form.html", context)


def registerUser(response):
    context = {}
    return render(response,"register_form.html", context)