# Generated by Django 3.2.4 on 2021-10-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_auto_20211017_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=6),
        ),
    ]
