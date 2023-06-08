# Generated by Django 4.1.2 on 2023-06-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("slno", models.CharField(max_length=250)),
                ("itemname", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]