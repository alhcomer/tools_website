# Generated by Django 4.2 on 2023-04-20 06:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("file_converter", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FileConverter",
            new_name="FileConversion",
        ),
    ]
