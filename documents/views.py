from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def documents(response):
    documents = Document.objects.all()
    context = {"documents": documents}
    return render(response, "documents/documents.html", context)


@login_required(login_url="login")
def add_document(response):
    form = DocumentForm()

    if response.method == "POST":
        if form.is_valid:
            form = DocumentForm(response.POST, response.FILES)
            form.save()
            redirect("documents")

    context ={"form": form}
    return render(response, "documents/document-form.html", context)


@login_required(login_url="login")
def change_document(response, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)

    if response.method == "POST":
        if response.is_valid:
            form = DocumentForm(response.POST, response.FILES, instance=document)
            document = form.save(commit=False)
            document.author = response.user.profile
            document.save()
            redirect("documents")
    context = {"form": form}
    return render(response, "documents/document-form.html", context)

