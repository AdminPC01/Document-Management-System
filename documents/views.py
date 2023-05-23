from django.shortcuts import render

# Create your views here.

def documents(response):
    # document = Document.objects.all()
    context = {}
    return render(response ,"main.html", context)

def document(response, pk):
    context = {}
    return render(response, "main.html", context)