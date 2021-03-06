# Generated by Django 3.0.5 on 2020-04-12 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_espn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='clap',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 12, 7, 2, 38, 620120)),
        ),
        migrations.AlterField(
            model_name='komen',
            name='tgl_komen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 12, 7, 2, 38, 620734)),
        ),
        migrations.AlterField(
            model_name='like',
            name='tgl_like',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 12, 7, 2, 38, 621363)),
        ),
    ]
