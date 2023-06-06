from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Department(models.Model):
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False),
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(default="profile_images/default-profile-image.png",
                                      upload_to="profile_images", null=True, blank=True)
    departmentID = models.ForeignKey(Department, max_length=200, null=True,
                                     blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

