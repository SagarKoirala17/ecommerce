# Generated by Django 3.0.2 on 2020-09-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_remove_contact_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
