# Generated by Django 5.2.1 on 2025-05-27 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('rdate', models.DateTimeField(blank=True, default=datetime.datetime(2025, 5, 27, 11, 36, 4, 122721))),
            ],
        ),
    ]
