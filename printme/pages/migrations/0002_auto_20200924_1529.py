# Generated by Django 3.0.2 on 2020-09-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='variety',
        ),
        migrations.DeleteModel(
            name='variety_type',
        ),
    ]
