# Generated by Django 4.2.1 on 2023-05-19 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('select_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mes',
            old_name='ID_mes',
            new_name='ID_dia',
        ),
        migrations.RenameField(
            model_name='mes',
            old_name='mes',
            new_name='dia',
        ),
        migrations.RenameField(
            model_name='semana',
            old_name='ID_dia',
            new_name='ID_mes',
        ),
        migrations.RenameField(
            model_name='semana',
            old_name='dia',
            new_name='mes',
        ),
    ]