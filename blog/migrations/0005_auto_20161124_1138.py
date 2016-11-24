# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-24 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161122_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
