from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from .forms import ResetForm
from .forms import NewName
from django.http import HttpResponseRedirect


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
            form = ResetForm(request.POST)
            if form.is_valid():
                newpassword=form.cleaned_data['new_pass1'],
                email=request.user.email
                password=form.cleaned_data['old_pass']

                user = authenticate(email=email, password=password)
                if user is not None:
                    user.set_password(newpassword)
                    user.save()
                    return redirect('profile')
                else:
                    return render(request, 'change_pass.html',{'error':'You have entered wrong old password','form': form})
            else:
                return render(request, 'change_pass.html',{'error':'You have entered old password','form': form})
        else:
            form = ResetForm()
        return render(request, 'change_pass.html', {'form': form})

    if(request.GET.get('cuser')):
        if request.method == 'POST':
            form = NewName(request.POST)
            if form.is_valid():
                newusername=form.cleaned_data['new_username']
                user.set_username(newusername)
                user.save()
                return redirect('profile')
            else:
                return render(request, 'new_username.html',{'error':'Enter a valid username','form': form})
        else:
            form = NewName()
        return render(request, 'new_username.html', {'form': form})

    return render(request, 'profile.html')
