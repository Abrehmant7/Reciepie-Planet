# Generated by Django 4.2.4 on 2023-10-31 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_todo_activity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='activity_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 12, 58, 58, 176240)),
        ),
    ]