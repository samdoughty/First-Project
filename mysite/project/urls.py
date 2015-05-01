from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='project/index.html'), name="Home"),
    #url(r'^login/', TemplateView.as_view(template_name='project/login.html'), name="Login"),
    url(r'^login/', views.Login, name="Login"),
    url(r'^logout/', views.Logout, name="Logout"),
    url(r'^register/', views.Register, name="Register"),
    url(r'^userprofile/(?P<pk>[0-9]+)', views.UserView.as_view(), name="UserProfile"),
    url(r'^jumps/', views.JumpsView.as_view(), name="Jumps"),
    url(r'^jump/(?P<pk>[0-9]+)', views.JumpView.as_view(), name="Jump"),
    url(r'^jump/edit/(?P<pk>[0-9]+)', views.EditJump, name="EditJump"),
]