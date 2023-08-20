# Generated by Django 4.2.4 on 2023-08-20 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_alter_creditcard_exp_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditcard",
            name="cvv",
            field=models.IntegerField(
                blank=True,
                validators=[
                    django.core.validators.MaxValueValidator(4),
                    django.core.validators.MinValueValidator(3),
                ],
            ),
        ),
    ]
