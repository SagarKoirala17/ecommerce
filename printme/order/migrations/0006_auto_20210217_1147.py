# Generated by Django 3.0.2 on 2021-02-17 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210216_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
