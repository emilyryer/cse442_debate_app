from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
import rooms



def room_render(request, roomName):
  client = storage.Client.from_service_account_json('creds.json')
  room = client.lookup_bucket(room_name)
  labels = room.labels
  joincode = int(labels[join-code])
  
    context = {'roomName':roomName,'joinCode':joincode}
  if room == None:
      raise Http404("Room with this room name does not exist.")
  else:
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
            #TODO: Handle error
            return 0
          elif(createStatus.startswith('NEW')): #NEW BUCKET CREATED
            return room_render(request, roomTopic)
          else: # Undefined behavior
            return 0
      return 0


def join(request):
    if(request.method == 'POST'):
      print("Request recieved to create a room.")
      if(request.user.is_authenticated ):
          print("User which made request is signed in.")
          ussername = request.user.nickName
          roomName = request.POST.get('roomname')
          roomID = request.POST.get('id')
          room = join_room(roomName, roomID)
          if room: #Something was returned, meaning we have been given a room.
            return redirect("/room/"+roomName+"/")