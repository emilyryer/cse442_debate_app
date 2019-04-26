from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nickName',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['nickName'].label = "Username"

class NewName(forms.Form):
    new_username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'username', 'placeholder':'New username',  'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(NewName, self).__init__(*args, **kwargs)
        self.fields['new_username'].label = "New username"

class DeleteAcc(forms.Form):
    del_email = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'email', 'placeholder':'email',  'class' : 'span'}))
    delpassword = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password',  'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(DeleteAcc, self).__init__(*args, **kwargs)
        self.fields['del_email'].label = "Email"
        self.fields['delpassword'].label = "Password"
