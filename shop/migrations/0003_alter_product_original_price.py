# Generated by Django 5.0.4 on 2024-04-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
