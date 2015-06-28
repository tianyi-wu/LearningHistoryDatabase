# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(max_length=10,primary_key=True)
    course_name = models.CharField(max_length=50, unique= True)
    a = models.DecimalField(u'基礎的素養',max_digits=5, decimal_places=2)
    b = models.DecimalField(u'専門性',max_digits=5, decimal_places=2)
    c = models.DecimalField(u'水平展開力',max_digits=5, decimal_places=2)
    d = models.DecimalField(u'設計力',max_digits=5, decimal_places=2)
    e = models.DecimalField(u'行動力',max_digits=5, decimal_places=2)
    weight = models.DecimalField(u'重み',max_digits=5, decimal_places=2)
    
    def __unicode__(self):
        return self.course_name


class Lecture(models.Model):
    gsdm_code = models.CharField(max_length=20,null=True,blank=True)
    category = models.CharField(max_length=20,null=True,blank=True)
    lecture_id =models.IntegerField(max_length=20,primary_key=True)
    lecture_name = models.CharField(max_length=50)
    term = models.CharField(max_length=10,null=True,blank=True)
    credit = models.IntegerField(max_length=10,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    specialization = models.CharField(max_length=50,null=True,blank=True)
    language = models.CharField(max_length=10,null=True,blank=True)
    teacher = models.CharField(max_length=50,null=True)
    other = models.CharField(max_length=100,null=True,blank=True)
    course = models.ForeignKey(Course)
    ifnormal = models.BooleanField(default=True)
        
    class Meta:
        #abstract = True
        ordering = ['lecture_name']
    
    def get_absolute_url(self):
        return reverse('lecture:detail', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return self.lecture_name
        




#class NormalLecture(Lecture):
    #def clean(self):
        #if self.course.course_id >= 6:
            #raise forms.ValidationError('The lecture is normal, not special.')


        
#class SpecialLecture(Lecture):
    #def clean(self):
        #if self.course.course_id <= 5:
            #raise forms.ValidationError('The lecture is special, not normal.')
