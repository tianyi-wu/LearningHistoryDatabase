# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('todai_id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('student_id_master', models.IntegerField(max_length=8, null=True)),
                ('student_id_docter', models.IntegerField(max_length=8, null=True)),
                ('ifautumn', models.BooleanField(default=False)),
                ('travel_fee_id', models.CharField(max_length=10, null=True)),
                ('trend_id', models.CharField(max_length=10, null=True)),
                ('shorekin13', models.CharField(max_length=10, null=True)),
                ('shorekin14', models.CharField(max_length=10, null=True)),
                ('sex', models.CharField(max_length=6, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])),
                ('department', models.CharField(max_length=20, choices=[('\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b', '\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b'), ('\u7dcf\u5408\u6cd5\u653f\u5c02\u653b', '\u7dcf\u5408\u6cd5\u653f\u5c02\u653b'), ('\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b', '\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b'), ('\u73fe\u4ee3\u7d4c\u6e08\u5c02\u653b', '\u7d4c\u6e08\u7406\u8ad6\u5c02\u653b'), ('\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b', '\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b'), ('\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b', '\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b'), ('\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b', '\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b'), ('\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b', '\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b'), ('\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b', '\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b'), ('\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b', '\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b'), ('\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b', '\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b'), ('\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b', '\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b'), ('\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b', '\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b'), ('\u8fb2\u5b66\u56fd\u969b\u5c02\u653b', '\u8fb2\u5b66\u56fd\u969b\u5c02\u653b'), ('\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b', '\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b'), ('\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b', '\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b'), ('\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b', '\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b'), ('\u793e\u4f1a\u533b\u5b66\u5c02\u653b', '\u793e\u4f1a\u533b\u5b66\u5c02\u653b'), ('\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b', '\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b'), ('\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b', '\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b')])),
                ('grade', models.CharField(max_length=3, choices=[('M1', 'M1'), ('M2', 'M2'), ('M3+', 'M3+'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5+', 'D5+')])),
                ('nationality', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('advising_teacher_department', models.CharField(max_length=20, choices=[('\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b', '\u516c\u5171\u653f\u7b56\u5b66\u5c02\u653b'), ('\u7dcf\u5408\u6cd5\u653f\u5c02\u653b', '\u7dcf\u5408\u6cd5\u653f\u5c02\u653b'), ('\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b', '\u91d1\u878d\u30b7\u30b9\u30c6\u30e0\u5c02\u653b'), ('\u73fe\u4ee3\u7d4c\u6e08\u5c02\u653b', '\u7d4c\u6e08\u7406\u8ad6\u5c02\u653b'), ('\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b', '\u793e\u4f1a\u57fa\u76e4\u5b66\u5c02\u653b'), ('\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b', '\u6a5f\u68b0\u5de5\u5b66\u5c02\u653b'), ('\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b', '\u7cbe\u5bc6\u5de5\u5b66\u5c02\u653b'), ('\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b', '\u822a\u7a7a\u5b87\u5b99\u5de5\u5b66\u5c02\u653b'), ('\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b', '\u96fb\u6c17\u7cfb\u5de5\u5b66\u5c02\u653b'), ('\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b', '\u30b7\u30b9\u30c6\u30e0\u5275\u6210\u5b66\u5c02\u653b'), ('\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b', '\u5316\u5b66\u30b7\u30b9\u30c6\u30e0\u5de5\u5b66\u5c02\u653b'), ('\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b', '\u539f\u5b50\u529b\u56fd\u969b\u5c02\u653b'), ('\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b', '\u6280\u8853\u7d4c\u55b6\u6226\u7565\u5b66\u5c02\u653b'), ('\u8fb2\u5b66\u56fd\u969b\u5c02\u653b', '\u8fb2\u5b66\u56fd\u969b\u5c02\u653b'), ('\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b', '\u8fb2\u696d\u30fb\u8cc7\u6e90\u7d4c\u6e08\u5b66\u5c02\u653b'), ('\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b', '\u30e1\u30c7\u30a3\u30ab\u30eb\u30b2\u30ce\u30e0\u5c02\u653b'), ('\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b', '\u56fd\u969b\u4fdd\u5065\u5b66\u5c02\u653b'), ('\u793e\u4f1a\u533b\u5b66\u5c02\u653b', '\u793e\u4f1a\u533b\u5b66\u5c02\u653b'), ('\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b', '\u96fb\u5b50\u60c5\u5831\u5b66\u5c02\u653b'), ('\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b', '\u5b66\u969b\u60c5\u5831\u5b66\u5c02\u653b')])),
                ('advising_teacher_name', models.CharField(max_length=50)),
                ('advising_teacher_email', models.EmailField(max_length=75, null=True)),
                ('sub_advising_teacher', models.CharField(max_length=75, null=True)),
                ('research_proposal', models.CharField(max_length=200, null=True)),
                ('other', models.CharField(max_length=200, null=True)),
                ('ifsummercamp', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
