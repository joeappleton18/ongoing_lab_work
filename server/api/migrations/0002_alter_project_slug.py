# Generated by Django 5.1.2 on 2024-10-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
