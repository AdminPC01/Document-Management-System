from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
# Create your views here.


def documents(response):
    documents = Document.objects.all()
    context = {"documents":documents}
    return render(response, "documents/documents.html", context)


def document(response, pk):
    document = Document.objects.get(id=pk)
    context = {"document": document}
    return render(response, "documents/singular-document.html", context)


def add_document(response):
    form = DocumentForm()

    if response.method == "POST":
        if form.is_valid:
            form = DocumentForm(response.POST, response.FILES)
            form.save()

    context ={"form": form}
    return render(response, "documents/document-form.html", context)


def change_document(response, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)

    if response.method == "POST":
        if response.is_valid:
            form = DocumentForm(response.POST, response.FILES, instance=document)
            document = form.save(commit=False)
            document.author = response.user.profile
            document.save()

    context = {"form": form}
    return render(response, "documents/document-form.html", context)

