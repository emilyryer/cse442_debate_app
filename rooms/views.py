from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic

def room_render(request, roomID):
  context = {'slug':roomID}
  return render(request, 'room.html', context)


def create(request):
   if(request.method == 'GET'):
    if(request.user.is_authenticated()):
      username = user.nicName()
      roomName = request.GET.get('roomname')
      roomTopic = request.GET.get('topic')
      createStatus = rooms.create_room(roomName, roomTopic, user)
      if(createStatus.startswith('Unable')): #Unable to make bucket
        #TODO: Handle error
        return 0
      elif(createStatus.startswith('Bucket')): #Bucket already exists
        #TODO: Handle e rror
        return 0
      elif(createStatus.startswith('NEW')): #NEW BUCKET CREATED
        return room_render(request, roomTopic)
      else: # Undefined behavior
        return 0
    return 0