# Generated by Django 2.2.6 on 2019-10-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_listing_listorgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='authToken',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='orgPassword',
            field=models.CharField(default='', max_length=100),
        ),
    ]
