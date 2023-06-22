from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    user = instance
    if created:
        employee = Employee.objects.create(
            user=user,
            name=user.first_name,
            username=user.username,
            email=user.email
        )


@receiver(post_delete, sender=Employee)
def delete_user(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()
