# Generated by Django 4.2.2 on 2023-07-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=150, unique=True)),
                ("author", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("number_of_copies", models.IntegerField(default=0)),
            ],
        ),
    ]
