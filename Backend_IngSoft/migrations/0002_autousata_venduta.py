# Generated by Django 5.0.6 on 2024-06-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Backend_IngSoft", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="autousata",
            name="venduta",
            field=models.BooleanField(default=False),
        ),
    ]
