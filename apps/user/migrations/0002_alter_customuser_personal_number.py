# Generated by Django 5.0.4 on 2024-04-23 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='personal_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Numero de personal'),
        ),
    ]
