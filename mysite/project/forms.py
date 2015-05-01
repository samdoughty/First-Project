from django import forms
from .models import Jump

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, error_messages={'required': 'Please enter a username.'})
    password = forms.CharField(widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please enter your password.'})
    remember = forms.BooleanField(required=False)

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100, error_messages={'required': 'Please enter a username.'})
	password = forms.CharField(widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please enter your password.'})
	email = forms.EmailField(error_messages={'required': 'Please enter your email.'})
	firstname = forms.CharField(label='First Name', max_length=100, error_messages={'required': 'Please enter your first name.'})
	lastname = forms.CharField(label='Last Name', max_length=100, error_messages={'required': 'Please enter your last name.'})
	jumpnumber = forms.IntegerField(error_messages={'required': 'Please enter your jump number.'})

class PostForm(forms.ModelForm):
    class Meta:
        model = Jump
        # exclude = ['author', 'updated', 'created', ]
        fields = ['TheDescription', 'Notes']
        #widgets = {
        #    'text': forms.TextInput(
        #        attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
        #    ),
        #}