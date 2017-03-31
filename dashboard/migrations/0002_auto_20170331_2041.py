# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('order_type', models.IntegerField()),
                ('locker_used', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.AlterModelOptions(
            name='prime',
            options={},
        ),
        migrations.AlterModelOptions(
            name='standard',
            options={},
        ),
        migrations.AlterModelOptions(
            name='table1',
            options={},
        ),
        migrations.AddField(
            model_name='orders',
            name='locker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Table1'),
        ),
    ]