# Generated by Django 4.1.5 on 2023-01-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="animal",
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
                ("specie_name", models.CharField(max_length=200)),
                ("habitatpk", models.IntegerField()),
                ("animal_image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="habitat",
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
                ("Region_Name", models.CharField(max_length=100)),
            ],
        ),
    ]