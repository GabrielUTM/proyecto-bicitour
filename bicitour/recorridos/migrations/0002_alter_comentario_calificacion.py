# Generated by Django 5.0.6 on 2024-08-17 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recorridos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='calificacion',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
