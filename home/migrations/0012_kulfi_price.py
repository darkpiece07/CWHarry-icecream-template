# Generated by Django 4.2.4 on 2023-09-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='kulfi',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
