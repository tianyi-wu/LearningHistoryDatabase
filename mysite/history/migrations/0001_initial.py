# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecture', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.CharField(max_length=8, choices=[('Summer', 'Summer'), ('Winter', 'Winter'), ('Allyear', 'Allyear')])),
                ('year', models.IntegerField(default=2014, max_length=4, choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('grade', models.CharField(max_length=2, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])),
                ('lecture', models.ForeignKey(to='lecture.Lecture')),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-year'],
            },
            bases=(models.Model,),
        ),
    ]
