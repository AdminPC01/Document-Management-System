import uuid

from django.db import models
# from django.db.models import Model
# Create your models here.

class Document(models.Model):

  #  author = models.ForeignKey(on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True),
    description = models.TextField( null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, )
    documents = models.FileField(null=True, blank=True, upload_to="documents")
    id = models.UUIDField(uuid.uuid4,unique=True, primary_key=True)

    def __str__(self):
        return str(self.title)

