# Generated by Django 3.0.2 on 2020-10-17 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200925_1300'),
        ('design', '0004_auto_20201017_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]