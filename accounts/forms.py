from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nickName',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['nickName'].label = "Username"

class ResetForm(forms.Form):
    old_pass = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'your old Password',  'class' : 'span'}))
    new_pass1 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'New Password',  'class' : 'span'}))
    new_pass2 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Confirm New Password',  'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(ResetForm, self).__init__(*args, **kwargs)
        self.fields['old_pass'].label = "Old password"
        self.fields['new_pass1'].label = "New password"
        self.fields['new_pass2'].label = "Confirm new password"

    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class NewName(forms.Form):
    new_username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'New username',  'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(NewName, self).__init__(*args, **kwargs)
        self.fields['new_username'].label = "New username"
