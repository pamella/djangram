from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserSignupForm
from users.models import User
from users.mixins import UserHasAccessToDetailMixin


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/detail_user.html'


class UserSignupView(generic.CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'users/signup_user.html'
    success_url = reverse_lazy('users:login_user')


class UserUpdateView(UserHasAccessToDetailMixin, generic.UpdateView):
    model = User
    fields = ['username', 'picture', ]
    template_name = 'users/update_user.html'

    def get_success_url(self):
        return reverse_lazy('users:detail_user', args=[self.object.pk])
