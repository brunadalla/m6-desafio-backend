# Generated by Django 4.1.5 on 2023-01-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactionsTypes", "0002_type_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="nature",
            field=models.CharField(
                choices=[("Entrada", "In"), ("Saída", "Out")],
                default="Entrada",
                max_length=24,
            ),
        ),
    ]