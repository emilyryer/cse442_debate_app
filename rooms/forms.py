from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from accounts.models import User


class CreateRoomForm(forms.Form):
    room_topic = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder':'Topic',  'class' : 'span'}))
    room_name = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder':'Name',  'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(CreateRoomForm, self).__init__(*args, **kwargs)
        self.fields['room_topic'].label = "Room Topic"
        self.fields['room_name'].label = "Room Name"



class JoinRoomForm(forms.Form):
    room_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Room ID', 'class' : 'span'}))

    def __init__(self, *args, **kwargs):
        super(JoinRoomForm, self).__init__(*args, **kwargs)
        self.fields['room_id'].label = "Room ID"

class DebateCheckForm(forms.Form):
    OPTIONS = [( 'Agree', 'Agree'),
              ( 'Disagree', 'Disagree')]

    opinion = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(DebateCheckForm, self).__init__(*args, **kwargs)
        self.fields['opinion'].label = "Opinion"

class CommentForm(forms.Form):
    comment = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'placeholder':'Comment',  'class' : 'span', 'size': 103}))

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = "Post Comment: "
