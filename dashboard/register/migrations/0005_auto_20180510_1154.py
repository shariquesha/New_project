# Generated by Django 2.0.4 on 2018-05-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20180509_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='Profile_Image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='user_details',
            name='Profile_Video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
