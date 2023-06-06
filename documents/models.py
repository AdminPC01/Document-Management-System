import uuid
from django.db import models
from users.models import Employee
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False)

    def __init__(self):
        return str(self.name)


class Document(models.Model):
    author = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True, blank=True)
    category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.CharField(max_length=200, null=True, blank=True)
    is_processed = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(null=True, blank=True, upload_to="documents")
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)



