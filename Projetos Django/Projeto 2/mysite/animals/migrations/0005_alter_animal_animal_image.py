# Generated by Django 4.1.5 on 2023-01-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0004_animal_votes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="animal_image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
