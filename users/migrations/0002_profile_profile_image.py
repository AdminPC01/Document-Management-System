# Generated by Django 4.1.6 on 2023-06-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default-profile-image.png', null=True, upload_to='profile_images'),
        ),
    ]