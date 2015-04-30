from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Dropzone
from .forms import LoginForm

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'project/index.html'

	def get_queryset(self):
		return Dropzone.objects.all()

def Login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/project/')
	else:
		form = LoginForm()

	return render(request, 'project/login.html', {'form': form})