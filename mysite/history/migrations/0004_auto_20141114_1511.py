# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_auto_20141114_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='other',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
