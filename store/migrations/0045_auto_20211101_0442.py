# Generated by Django 3.2.4 on 2021-11-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_product_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add',
        ),
        migrations.AddField(
            model_name='product',
            name='adds',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
