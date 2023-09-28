# Generated by Django 4.2.4 on 2023-09-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='static/avatar.png', height_field='200', upload_to='profile_pics/', width_field='200'),
        ),
    ]
