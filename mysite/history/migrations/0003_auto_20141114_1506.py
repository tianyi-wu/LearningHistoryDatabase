# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_history_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='other',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]
