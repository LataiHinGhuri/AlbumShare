# Generated by Django 2.0.4 on 2018-04-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=250)),
                ('album_message', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
