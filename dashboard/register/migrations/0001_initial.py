# Generated by Django 2.0.4 on 2018-05-08 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Street_Name', models.CharField(max_length=100)),
                ('City_Name', models.CharField(max_length=100)),
                ('State_Name', models.CharField(max_length=100)),
                ('Country_Name', models.CharField(max_length=100)),
                ('PinCode', models.IntegerField()),
                ('Mobile_Number', models.IntegerField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
