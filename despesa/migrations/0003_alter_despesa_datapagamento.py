# Generated by Django 4.1.3 on 2024-05-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0002_despesa_datapagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='dataPagamento',
            field=models.DateField(),
        ),
    ]
