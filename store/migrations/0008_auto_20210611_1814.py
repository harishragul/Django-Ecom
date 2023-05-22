# Generated by Django 3.2.4 on 2021-06-11 18:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_shippingaddress_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(default=datetime.datetime(2021, 6, 11, 18, 14, 24, 598478, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='number',
            field=models.CharField(default=datetime.datetime(2021, 6, 11, 18, 14, 41, 344261, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]