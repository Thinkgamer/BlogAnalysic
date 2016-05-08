# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('user_viewnum', models.CharField(max_length=100, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe6\x80\xbb\xe9\x87\x8f')),
                ('user_jifen', models.CharField(max_length=100, verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe7\xa7\xaf\xe5\x88\x86')),
                ('user_blognum', models.CharField(max_length=100, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\x80\xbb\xe6\x95\xb0')),
                ('user_fromnum', models.IntegerField(verbose_name=b'\xe8\xbd\xac\xe8\xbd\xbd\xe6\x95\xb0\xe7\x9b\xae')),
                ('user_fanyinum', models.IntegerField(verbose_name=b'\xe7\x96\x91\xe9\x97\xae\xe6\x95\xb0\xe7\x9b\xae')),
                ('user_disnum', models.IntegerField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0\xe7\x9b\xae')),
                ('user_focusnum', models.IntegerField(verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe4\xba\xba\xe6\x95\xb0')),
                ('user_fansnum', models.IntegerField(verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe4\xba\xba\xe6\x95\xb0')),
                ('user_focusid', models.TextField(verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe5\x88\x97\xe8\xa1\xa8')),
                ('user_fansid', models.TextField(verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe5\x88\x97\xe8\xa1\xa8')),
            ],
            options={
                'db_table': 'userMessage',
            },
        ),
        migrations.CreateModel(
            name='UserNum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('user_id', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID')),
            ],
        ),
    ]
