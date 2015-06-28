# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20141114_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='student_id_docter',
            field=models.IntegerField(max_length=8, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe7\x95\xaa\xe5\x8f\xb7\xef\xbc\x88\xe5\x8d\x9a\xe5\xa3\xab\xef\xbc\x89', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_id_master',
            field=models.IntegerField(max_length=8, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe7\x95\xaa\xe5\x8f\xb7\xef\xbc\x88\xe4\xbf\xae\xe5\xa3\xab\xef\xbc\x89', blank=True),
        ),
    ]
