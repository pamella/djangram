from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import generic

from users.models import User

class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass

class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/detail_user.html'