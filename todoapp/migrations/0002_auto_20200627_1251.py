# Generated by Django 3.0.7 on 2020-06-27 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 12, 51, 8, 893659)),
        ),
    ]