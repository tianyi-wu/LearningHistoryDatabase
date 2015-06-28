# coding: UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from account.models import UserProfile
from history.models import History
from lecture.models import Lecture,Course
from decimal import *

# Create your models here.
class Score(models.Model):
	user_profile = models.OneToOneField(UserProfile, default=None)
	a = models.DecimalField(default=0, max_digits=65, decimal_places=2)
	b = models.DecimalField(default=0, max_digits=65, decimal_places=2)
	c = models.DecimalField(default=0, max_digits=65, decimal_places=2)
	d = models.DecimalField(default=0, max_digits=65, decimal_places=2)
	e = models.DecimalField(default=0, max_digits=65, decimal_places=2)

	def set_user(self, user_id):
		self.user_profile = UserProfile.objects.get(user_id = user_id)

	@classmethod
	def get_score(cls, user_id):
		try:
			score = Score.objects.get(user_profile__user_id = user_id)
		except ObjectDoesNotExist:
			score = Score()
			score.set_user(user_id)
		return score

	def calc_score(self):
		user_profile = UserProfile.objects.get(user_id=self.user_profile.user_id)
		user_histories = History.objects.filter(student__id = self.user_profile.user_id)
		try:
			score = Score.objects.get(user_profile = self.user_profile)
		except ObjectDoesNotExist:
			score = self
		a = Decimal(0)
		b = Decimal(0)
		c = Decimal(0)
		d = Decimal(0)
		e = Decimal(0)
		for history in user_histories:
			weight = history.lecture.course.weight
			a += history.lecture.course.a * weight
			b += history.lecture.course.b * weight
			c += history.lecture.course.c * weight
			d += history.lecture.course.d * weight
			e += history.lecture.course.e * weight
		score.a = a
		score.b = b
		score.c = c
		score.d = d
		score.e = e
		score.save()
