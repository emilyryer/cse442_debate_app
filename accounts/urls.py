# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from .views import profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
