# Generated by Django 3.0.2 on 2020-03-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(),
        ),
    ]
