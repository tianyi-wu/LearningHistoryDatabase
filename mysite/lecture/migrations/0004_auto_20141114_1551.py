# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20141114_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='department',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
