# Generated by Django 4.1.3 on 2024-05-01 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='dataPagamento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
