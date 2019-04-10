from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from rooms import rooms
from rooms import views


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

  
def request_page(request):
  if(request.GET.get('createbtn')):
    if(request.user.is_authenticated()):
      username = user.nicName()
      roomName = request.GET.get('createName')
      roomTopic = request.GET.get('createTopic')
      createStatus = rooms.create_room(roomName, roomTopic, user)
      if(createStatus.startswith('Unable')): #Unable to make bucket
        #TODO: Handle error
        return 0
      elif(createStatus.startswith('Bucket')): #Bucket already exists
        #TODO: Handle error
        return 0
      elif(createStatus.startswith('NEW')): #NEW BUCKET CREATED
        return rooms.views.room_render(request, roomTopic)
      else: # Undefined behavior
        return 0