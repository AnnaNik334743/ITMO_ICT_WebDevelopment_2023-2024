# Generated by Django 4.2.5 on 2023-09-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="date_of_birth",
            field=models.DateTimeField(null=True),
        ),
    ]