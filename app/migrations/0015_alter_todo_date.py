# Generated by Django 4.2.4 on 2023-11-02 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 18, 31, 6, 278743)),
        ),
    ]
