# Generated by Django 4.1.5 on 2023-01-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0003_habitat_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="votes",
            field=models.IntegerField(default=0),
        ),
    ]
