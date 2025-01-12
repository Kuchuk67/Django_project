# Generated by Django 5.1.4 on 2025-01-12 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category_name", models.CharField(max_length=150, verbose_name="категория")),
                ("description", models.TextField(verbose_name="описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["category_name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="наименование")),
                ("description", models.TextField(verbose_name="описание")),
                ("image", models.ImageField(upload_to="images/", verbose_name="изображение")),
                ("price", models.IntegerField(verbose_name="цена")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="дата создания")),
                ("updated_at", models.DateTimeField(auto_now_add=True, verbose_name="дата последнего изменения")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="category", to="catalog.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["created_at"],
            },
        ),
    ]
