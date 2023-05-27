from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
# Create your views here.

def Documents(response):
    document = Document.objects.all()
    context = {}
    return render(response ,"main.html", context)

def Document(response, pk):
    document = Document.objects.get(id=pk)
    context = {}
    return render(response, "main.html", context)


def addDocument(response):
    form = DocumentForm()

    if response.method == "POST":
        if response.valid():
            form = DocumentForm(response.POST, response.FILES)
            form.save()

    context ={"form": form}
    return render(response, "documents/document-form.html", context)


def changeDocument(response, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)

    if response.method == "POST":
        if response.valid():
            form = DocumentForm(response.POST, response.FILES, instance=document)
            document = form.save(commit=False)
            document.author = response.user.profile
            document.save()

    context = {"form": form}
    return render(response, "documents/document-form.html", context)

