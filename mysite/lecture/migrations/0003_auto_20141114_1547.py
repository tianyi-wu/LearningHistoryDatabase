# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_auto_20141114_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='category',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='credit',
            field=models.IntegerField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='language',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='other',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='specialization',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='term',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
