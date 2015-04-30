from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, error_messages={'required': 'Please enter a username.'})
    password = forms.CharField(widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please enter your password.'})
    remember = forms.BooleanField(required=False)