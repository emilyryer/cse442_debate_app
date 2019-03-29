# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from .views import profile

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
