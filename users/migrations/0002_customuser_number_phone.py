# Generated by Django 5.1.4 on 2025-02-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="number_phone",
            field=models.CharField(blank=True, max_length=20, verbose_name="телефон"),
        ),
    ]
