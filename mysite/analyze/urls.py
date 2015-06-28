from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from analyze import views

#from lecture import views
urlpatterns = patterns('',
	url(r'^$', 'analyze.views.analyze', name='analyze'),
)
