# Generated by Django 2.2.6 on 2019-11-14 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_listing_listdeadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='authToken',
        ),
    ]