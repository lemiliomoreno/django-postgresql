# Generated by Django 4.2.2 on 2023-06-23 01:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0003_locations"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Locations",
        ),
    ]
