# Generated by Django 3.2 on 2022-01-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
