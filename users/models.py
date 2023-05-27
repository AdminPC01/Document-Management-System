from django.db import models
from django.db.models import User
# Create your models here.


class Profile(models.Model):
    user = models.Foreignkey(User, on_delete=models.CASCADE, null=True, bank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    post = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)
