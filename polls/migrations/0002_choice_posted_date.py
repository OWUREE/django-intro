# Generated by Django 2.2.5 on 2019-09-18 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 9, 18, 10, 0, 15, 715108, tzinfo=utc)),
            preserve_default=False,
        ),
    ]