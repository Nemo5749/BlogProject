# Generated by Django 2.2.6 on 2019-11-13 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='citeFrom',
            field=models.TextField(blank=True, verbose_name='参考资料'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 14, 18, 13, 904750), verbose_name='创建时间'),
        ),
    ]
