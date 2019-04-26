from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from .forms import DeleteAcc
from .forms import NewName
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from accounts.models import User
from django.contrib import messages


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


def profile(request):
    if(request.GET.get('cpass')):
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                oldpass = form.cleaned_data['old_password']
                newpass = form.cleaned_data['new_password1']
                if (oldpass == newpass):
                    print(form.error_messages)
                    messages.error(request, 'You cant use your old password')
                else:
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return redirect('/accounts/profile')
            else:
                print(form.error_messages)
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_pass.html', {'form': form})

    if(request.GET.get('cuser')):
        if request.method == 'POST':
            form = NewName(request.POST)
            if form.is_valid():
                newusername=form.cleaned_data['new_username']
                email=request.user.email
                user = User.objects.get(email = email)
                user.set_username(newusername)
                user.save()
                return redirect('profile')
            else:
                return render(request, 'new_username.html',{'error':'Enter a valid username','form': form})
        else:
            form = NewName()
        return render(request, 'new_username.html', {'form': form})

    if(request.GET.get('deleteacc')):
        if request.method == 'POST':
            form = DeleteAcc(request.POST)
            if form.is_valid():
                email=request.user.email
                user = authenticate(email=form.cleaned_data['del_email'], password=form.cleaned_data['delpassword'])
                if user is None:
                    print("does not exhist")
                    messages.error(request,'username or password not correct')
                    return render(request,'delete_acc.html', {'form' : form})
                else:
                    user = User.objects.get(email = email)
                    user.delete()
                    update_session_auth_hash(request, user)
                    print("deleted")
                    return redirect('home')
            else:
                print("not valid")
                return render(request, 'delete_acc.html',{'error':'Enter a valid username','form': form})
        else:
            form = DeleteAcc()
        return render(request, 'delete_acc.html', {'form': form})

    return render(request, 'profile.html')
