# Generated by Django 2.0.4 on 2018-05-10 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20180510_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='Profile_Video',
        ),
    ]
