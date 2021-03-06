# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0011_auto_20160410_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('contents_count', models.IntegerField(default=0)),
                ('follow_count', models.IntegerField(default=0)),
                ('follower_count', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=2)),
                ('intro', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'photos/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_username',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contents',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contents',
            name='content_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contents',
            name='username',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='follows',
            name='follow_username',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='follows',
            name='username',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
