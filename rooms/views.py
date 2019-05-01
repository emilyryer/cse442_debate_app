from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from accounts.models import User
from django.contrib import messages
from django import forms
from .forms import CreateRoomForm
from .forms import JoinRoomForm
from .forms import DebateCheckForm
from .forms import CommentForm

def create(request, id):
        if request.method == 'POST':
            form = CreateRoomForm(request.POST)
            if form.is_valid():
                userid = request.user.id
                roomName = form.cleaned_data['room_name']
                roomTopic = form.cleaned_data['room_topic']
                context = {
                    'roomName': roomName,
                    'roomTopic': roomTopic,
                    }
                request.session['room-name'] = roomName
                request.session['room-topic'] = roomTopic
                return redirect(roomName + '/')
            else:
              print(form.errors.as_text())
              print("nada")
        else:
            form = CreateRoomForm(request.POST)
        return render(request, 'create-room.html', {'form': form})

def join(request):
        if request.method == 'POST':
            form = JoinRoomForm(request.POST)
            if form.is_valid():
                userid = request.user.id
                room_id = form.cleaned_data['room_id']
                context = {
                    'room_id': room_id,
                    }
                request.session['room-topic'] = "Social Media"
                request.session['room-name'] = "Should social media platfroms be responsible for user uploaded content?"
                print("gotcha")
                return redirect('24335/Social Media/')
            else:
              print(form.errors.as_text())
              print("nada")
        else:
            form = CreateRoomForm(request.POST)
        return render(request, 'join-room.html', {'form': form})

def room(request, id, string):
    if request.method == 'POST':
        form = DebateCheckForm(request.POST)
        cForm = CommentForm(request.POST)
        if form.is_valid():
            opinion = form.cleaned_data['opinion']
            request.session['opinion'] = opinion
            room_name = request.session.get('room-name')
            room_topic = request.session.get('room-topic')
            context = {
                'opinion': opinion,
                'roomName': room_name,
                'roomTopic': room_topic,
                'cForm': cForm
                }
            return render(request, 'room.html', context )
        elif cForm.is_valid():
            print("made it")
            opinion = request.session.get('opinion')
            comment = cForm.cleaned_data['comment']
            room_name = request.session.get('room-name')
            room_topic = request.session.get('room-topic')
            context = {
                'opinion' : opinion,
                'roomName': room_name,
                'roomTopic': room_topic,
                'cForm': cForm,
                'comment': comment
                }
            print("made it")
            return render(request, 'room.html', context )
        else:
          print(form.errors.as_text())
          print("nada")
    else:
        form = DebateCheckForm(request.POST)
        room_name = request.session.get('room-name')
        room_topic = request.session.get('room-topic')
        context = {
            'roomName': room_name,
            'roomTopic': room_topic,
            'form': form
            }
    return render(request, 'room.html', context )
