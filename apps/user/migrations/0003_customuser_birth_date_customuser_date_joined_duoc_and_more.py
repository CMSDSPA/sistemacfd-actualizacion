# Generated by Django 5.0.4 on 2024-06-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_personal_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined_duoc',
            field=models.DateField(null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='img_profile',
            field=models.ImageField(blank=True, default='/img/profile.webp', null=True, upload_to='', verbose_name='Imagen de perfil'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mother_surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellido de la madre'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='rut',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Rut'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='secondary_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email secundario'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='url_linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='URL de linkedin'),
        ),
    ]