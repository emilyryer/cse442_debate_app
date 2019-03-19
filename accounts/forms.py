from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.forms as forms
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nickName',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['nickName'].label = "Username"
