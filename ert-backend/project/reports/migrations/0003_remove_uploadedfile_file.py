# Generated by Django 2.2.1 on 2020-04-21 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200421_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='file',
        ),
    ]
