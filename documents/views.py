from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from users.models import Employee
from .utils import search_documents
# Create your views here.


@login_required(login_url="login")
def documents(response):

    documents, search_query = search_documents(response)
    user = response.user
    employee = Employee.objects.get(user=user)

    context = {"employee": employee, "documents": documents}
    return render(response, "documents/documents.html", context)


@login_required(login_url="users/login-registration.html")
@permission_required('document.add_document', login_url="users/login-registration.html")
def add_document(response):
    form = DocumentForm()
    user = response.user
    employee = Employee.objects.get(user=user)
    if response.method == "POST":
        if form.is_valid:
            form = DocumentForm(response.POST, response.FILES)
            document = form.save(commit=False)
            document.author = employee
            document.save()
    redirect("documents")


    context = {"form": form, "employee": employee}
    return render(response, "documents/document-form.html", context)


@login_required(login_url="login")
@permission_required("document.change_document", login_url="users/login-registration.html")
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

    user = response.user
    employee = Employee.objects.get(user=user)
    context = {"form": form, "employee": employee}

    return render(response, "documents/document-form.html", context)

