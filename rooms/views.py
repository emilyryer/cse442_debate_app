from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
import rooms

def room_render(request, roomID):
  context = {'slug':roomID}
  return render(request, 'room.html', context)


def create(request):
  if(request.method == 'POST'):
      print("Request recieved to create a room.")
  if(request.user.is_authenticated ):
      print("User which made request is signed in.")
      username = request.user.nickName
      roomName = request.POST.get('roomname')
      roomTopic = request.POST.get('topic')       
      createStatus = rooms.create_room(room_name=roomName, topic=roomTopic, user=username)
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
