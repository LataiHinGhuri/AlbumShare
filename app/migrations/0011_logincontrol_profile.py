# Generated by Django 2.0.4 on 2018-05-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_logincontrol'),
    ]

    operations = [
        migrations.AddField(
            model_name='logincontrol',
            name='profile',
            field=models.CharField(default='My Profile', max_length=50),
        ),
    ]