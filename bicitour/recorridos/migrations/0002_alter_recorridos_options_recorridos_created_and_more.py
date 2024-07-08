# Generated by Django 5.0.6 on 2024-07-08 07:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recorridos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recorridos',
            options={'ordering': ['-created'], 'verbose_name': 'Recorrido', 'verbose_name_plural': 'Recorridos'},
        ),
        migrations.AddField(
            model_name='recorridos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorridos',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
