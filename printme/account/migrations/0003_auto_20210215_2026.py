# Generated by Django 3.0.2 on 2021-02-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200925_1300'),
        ('account', '0002_auto_20210215_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='design',
        ),
        migrations.AddField(
            model_name='profile',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
    ]