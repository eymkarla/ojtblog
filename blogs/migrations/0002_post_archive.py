# Generated by Django 2.0.5 on 2018-07-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
