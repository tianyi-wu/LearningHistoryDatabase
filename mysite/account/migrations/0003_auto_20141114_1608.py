# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20141114_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='advising_teacher_department',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe6\x8c\x87\xe5\xb0\x8e\xe6\x95\x99\xe5\x93\xa1\xe5\xb0\x82\xe6\x94\xbb', choices=[('\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b', '\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b'), ('\u7dcf\u5408\u6cd5\u653f\u5c02\u653b', '\u7dcf\u5408\u6cd5\u653f\u5c02\u653b'), ('\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b', '\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b'), ('\u73fe\u4ee3\u7d4c\u6e08\u5c02\u653b', '\u7d4c\u6e08\u7406\u8ad6\u5c02\u653b'), ('\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b', '\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b'), ('\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b', '\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b'), ('\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b', '\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b'), ('\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b', '\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b'), ('\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b', '\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b'), ('\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b', '\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b'), ('\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b', '\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b'), ('\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b', '\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b'), ('\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b', '\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b'), ('\u8fb2\u5b66\u56fd\u969b\u5c02\u653b', '\u8fb2\u5b66\u56fd\u969b\u5c02\u653b'), ('\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b', '\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b'), ('\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b', '\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b'), ('\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b', '\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b'), ('\u793e\u4f1a\u533b\u5b66\u5c02\u653b', '\u793e\u4f1a\u533b\u5b66\u5c02\u653b'), ('\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b', '\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b'), ('\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b', '\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='advising_teacher_email',
            field=models.EmailField(max_length=75, null=True, verbose_name=b'\xe6\x8c\x87\xe5\xb0\x8e\xe6\x95\x99\xe5\x93\xa1\xe3\x83\xa1\xe3\x83\xbc\xe3\x83\xab\xe3\x82\xa2\xe3\x83\x89\xe3\x83\xac\xe3\x82\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='advising_teacher_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x8c\x87\xe5\xb0\x8e\xe6\x95\x99\xe5\x93\xa1\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xb0\x82\xe6\x94\xbb', choices=[('\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b', '\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b'), ('\u7dcf\u5408\u6cd5\u653f\u5c02\u653b', '\u7dcf\u5408\u6cd5\u653f\u5c02\u653b'), ('\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b', '\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b'), ('\u73fe\u4ee3\u7d4c\u6e08\u5c02\u653b', '\u7d4c\u6e08\u7406\u8ad6\u5c02\u653b'), ('\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b', '\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b'), ('\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b', '\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b'), ('\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b', '\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b'), ('\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b', '\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b'), ('\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b', '\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b'), ('\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b', '\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b'), ('\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b', '\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b'), ('\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b', '\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b'), ('\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b', '\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b'), ('\u8fb2\u5b66\u56fd\u969b\u5c02\u653b', '\u8fb2\u5b66\u56fd\u969b\u5c02\u653b'), ('\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b', '\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b'), ('\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b', '\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b'), ('\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b', '\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b'), ('\u793e\u4f1a\u533b\u5b66\u5c02\u653b', '\u793e\u4f1a\u533b\u5b66\u5c02\u653b'), ('\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b', '\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b'), ('\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b', '\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'\xe3\x83\xa1\xe3\x83\xbc\xe3\x83\xab\xe3\x82\xa2\xe3\x83\x89\xe3\x83\xac\xe3\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='grade',
            field=models.CharField(max_length=3, verbose_name=b'\xe5\xad\xa6\xe5\xb9\xb4', choices=[('M1', 'M1'), ('M2', 'M2'), ('M3+', 'M3+'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5+', 'D5+')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ifautumn',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xa7\x8b\xe5\x85\xa5\xe5\xad\xa6'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x9b\xbd\xe7\xb1\x8d'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='other',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe3\x81\x9d\xe3\x81\xae\xe4\xbb\x96\xe7\x89\xb9\xe8\xa8\x98\xe4\xba\x8b\xe9\xa0\x85', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='research_proposal',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xa0\x94\xe7\xa9\xb6\xe3\x83\x86\xe3\x83\xbc\xe3\x83\x9e', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=6, verbose_name=b'\xe6\x80\xa7\xe5\x88\xa5', choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='todai_id',
            field=models.IntegerField(max_length=10, serialize=False, verbose_name=b'\xe5\xad\xa6\xe7\xb1\x8d\xe7\x95\xaa\xe5\x8f\xb7', primary_key=True),
        ),
    ]
