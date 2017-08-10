# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='todoList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.TodoList'),
        ),
    ]
