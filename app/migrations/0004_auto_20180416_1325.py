# Generated by Django 2.0.4 on 2018-04-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comments_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='images',
            field=models.FileField(upload_to='media/', verbose_name='Document'),
        ),
    ]