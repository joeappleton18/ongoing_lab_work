# Generated by Django 5.0 on 2024-10-21 09:55

import api.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, unique=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=256, null=True),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="media")),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                ("position", models.PositiveIntegerField()),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.board"
                    ),
                ),
            ],
            options={
                "unique_together": {("board", "title")},
            },
        ),
        migrations.CreateModel(
            name="Label",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32)),
                (
                    "colour",
                    models.CharField(
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator("#[0-9A-F]{6}")
                        ],
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.project"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="board",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.project"
            ),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("task_no", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=64)),
                (
                    "description",
                    models.TextField(blank=True, max_length=512, null=True),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("H", "High"), ("M", "Medium"), ("L", "Low")],
                        max_length=1,
                    ),
                ),
                (
                    "story_points",
                    models.PositiveIntegerField(
                        validators=[api.models.Task.validate_story_points]
                    ),
                ),
                ("labels", models.ManyToManyField(to="api.label")),
                (
                    "list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.list"
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="board",
            unique_together={("project", "title")},
        ),
    ]
