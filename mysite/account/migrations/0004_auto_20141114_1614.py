# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20141114_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ifsummercamp',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe3\x82\xb5\xe3\x83\x9e\xe3\x83\xbc\xe3\x82\xad\xe3\x83\xa3\xe3\x83\xb3\xe3\x83\x97\xe5\xbf\x9c\xe5\x8b\x9f', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='research_proposal',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xa0\x94\xe7\xa9\xb6\xe8\xaa\xb2\xe9\xa1\x8c', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shorekin13',
            field=models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xa5\xa8\xe5\x8a\xb1\xe9\x87\x9113', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shorekin14',
            field=models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xa5\xa8\xe5\x8a\xb1\xe9\x87\x9114', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sub_advising_teacher',
            field=models.CharField(max_length=75, null=True, verbose_name=b'\xe5\x89\xaf\xe6\x8c\x87\xe5\xb0\x8e\xe6\x95\x99\xe5\x93\xa1\xe3\x81\xae\xe5\xb8\x8c\xe6\x9c\x9b', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='travel_fee_id',
            field=models.CharField(max_length=10, null=True, verbose_name=b'\xe6\x97\x85\xe8\xb2\xbb\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6ID', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trend_id',
            field=models.CharField(max_length=10, null=True, verbose_name=b'\xe5\x8f\x96\xe5\xbc\x95\xe5\x85\x88\xe3\x82\xb3\xe3\x83\xbc\xe3\x83\x89', blank=True),
        ),
    ]
