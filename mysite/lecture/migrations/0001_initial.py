# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('course_name', models.CharField(unique=True, max_length=50)),
                ('a', models.DecimalField(max_digits=5, decimal_places=2)),
                ('b', models.DecimalField(max_digits=5, decimal_places=2)),
                ('c', models.DecimalField(max_digits=5, decimal_places=2)),
                ('d', models.DecimalField(max_digits=5, decimal_places=2)),
                ('e', models.DecimalField(max_digits=5, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('gsdm_code', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('lecture_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('lecture_name', models.CharField(max_length=50)),
                ('term', models.CharField(max_length=10)),
                ('credit', models.IntegerField(max_length=10)),
                ('department', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=100)),
                ('ifnormal', models.BooleanField(default=True)),
                ('course', models.ForeignKey(to='lecture.Course')),
            ],
            options={
                'ordering': ['lecture_name'],
            },
            bases=(models.Model,),
        ),
    ]
