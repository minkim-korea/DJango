# Generated by Django 5.2.1 on 2025-05-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuscore',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('kor', models.IntegerField(default=0)),
                ('eng', models.IntegerField(default=0)),
                ('math', models.IntegerField(default=0)),
                ('title', models.IntegerField(default=0)),
                ('avg', models.IntegerField(default=0)),
            ],
        ),
    ]
