# Generated by Django 4.2.1 on 2023-06-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='is_processed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
