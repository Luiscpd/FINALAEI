# Generated by Django 4.2.1 on 2023-05-13 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_remove_datosusuario_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosusuario',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
