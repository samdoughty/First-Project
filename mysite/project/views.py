from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import json

from .models import Jump, UserProfile, Dropzone
from .forms import LoginForm, RegisterForm

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'project/index.html'

	def get_queryset(self):
		return Dropzone.objects.all()

class UserView(generic.DetailView):
	template_name = 'project/user.html'
	model = UserProfile

class JumpsView(generic.ListView):
	template_name = 'project/jumps.html'
	context_object_name = 'jumps'

	def get_queryset(self):
		return Jump.objects.all()

class JumpView(generic.DetailView):
	template_name = 'project/jump.html'
	model = Jump

def EditJump(request, pk):
	if request.method == 'POST':
		p = get_object_or_404(Jump, pk=pk)
		p.TheDescription = request.POST.get("Description")
		p.Notes = request.POST.get("Notes")
		p.save()
		response_data = {}

		response_data["TheDescription"] = p.TheDescription
		response_data["Notes"] = p.Notes
		return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def Login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/project/')
				else:
					form.add_error(None, "Your account has been disabled.")
			else:
				form.add_error(None, "Invalid username or password.")
	else:
		form = LoginForm()

	return render(request, 'project/login.html', {'form': form})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/project/')

def Register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			user.first_name = request.POST['firstname']
			user.last_name = request.POST['lastname']
			user.Save()
			userProfile = UserProfile.objects.create(UserID=user, JumpNumber=request.POST['jumpnumber'])
			if user is not None:
				if userProfile is not None:
					return HttpResponseRedirect('/project/')
				else:
					form.add_error(None, "Error creating your User Profile")
			else:
				form.add_error(None, "Error creating your User")
	else:
		form = RegisterForm()
	return render(request, 'project/register.html', {'form':form})