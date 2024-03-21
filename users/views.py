from allauth.account.views import PasswordChangeView as allauth_PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PasswordChangeView(allauth_PasswordChangeView):
    success_url = reverse_lazy('home')
