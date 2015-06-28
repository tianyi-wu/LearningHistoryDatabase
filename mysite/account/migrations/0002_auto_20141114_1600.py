# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='advising_teacher_email',
            field=models.EmailField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ifsummercamp',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='other',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='research_proposal',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shorekin13',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shorekin14',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_id_docter',
            field=models.IntegerField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_id_master',
            field=models.IntegerField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sub_advising_teacher',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='travel_fee_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trend_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
