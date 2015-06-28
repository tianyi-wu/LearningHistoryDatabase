# coding:utf-8

from django.core.urlresolvers import reverse
from django.db import models

#from django.core.exceptions import ValidationError

import datetime

from lecture.models import Lecture
#,NormalLecture,SpecialLecture
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):
    GRADE_CHOICES = (
        (u'S', u'S'),
        (u'A', u'A'),
        (u'B', u'B'),
        (u'C', u'C'),
        (u'D', u'D'),
    )

    YEAR_CHOICES = []
    for r in range(2010, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    TERM_CHOICES =(
        (u'Summer',u'Summer'),
        (u'Winter',u'Winter'),
        (u'Allyear',u'Allyear'),
        )
        
    term = models.CharField(max_length=8, choices=TERM_CHOICES)

    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    lecture = models.ForeignKey(Lecture)
    student = models.ForeignKey(User)
    other = models.CharField(max_length=255, default="",null=True,blank=True)

    class Meta:
        # abstract = True
        ordering = ["-year"]

    def get_absolute_url(self):
        return reverse('history:detail', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return u'%s %s %s %s' % (self.student, self.lecture, self.year, self.grade)

    def is_registrated(lecture_id):
        registrated_list = History.objects.filter(student = self.student)
        for i in registrated_list:
            if i.lecture.lecture_id == lecture_id:
                return True
        return False
# class NormalHistory(History):
#     def clean(self):
#         if self.lecture.course.course_id > 5:
#             raise ValidationError('The lecture is special, not normal.')

#     class Meta:
#         unique_together = ('student', 'lecture')


# class SpecialHistory(History):
#     def clean(self):
#         if self.lecture.course.course_id <= 5:
#             raise ValidationError('The lecture is special, not normal.')

