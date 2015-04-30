from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='project/index.html'), name="Home"),
    #url(r'^login/', TemplateView.as_view(template_name='project/login.html'), name="Login"),
    url(r'^login/', views.Login, name="Login")
]