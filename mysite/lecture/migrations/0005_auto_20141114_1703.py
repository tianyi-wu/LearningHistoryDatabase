# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_auto_20141114_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='gsdm_code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
