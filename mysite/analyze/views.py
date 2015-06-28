from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth import authenticate, login, get_user_model

from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import logout

from django.views import generic

from mysite.views import LoginRequiredMixin

from account.forms import UserForm, UserProfileForm
from account.models import UserProfile

from analyze.models import Score 

# Create your views here.
def analyze(request):
	score = Score()
	score.set_user(user_id = request.user.id)
	score.calc_score()
	score = Score.objects.get(user_profile = score.user_profile)
	data = { 
		'score' : score,
	 }
	return render_to_response('analyze/index.html',data,context_instance=RequestContext(request))
