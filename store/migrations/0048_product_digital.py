# Generated by Django 3.2.4 on 2022-01-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_auto_20220118_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
