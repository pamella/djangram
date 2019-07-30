from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserSignupForm
from users.helpers import send_confirm_user_signup_email
from users.mixins import UserHasAccessToDetailMixin
from users.models import User


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

    def form_valid(self, form):
        # equivalente nesse caso
        # self.object = form.save()
        # commit=False quando se quer adicionar outros atributos (fora os do form)
        # antes de salvar de fato
        self.object = form.save(commit=False)
        self.object.save()
        send_confirm_user_signup_email(self.object)
        return super().form_valid(form)


class UserUpdateView(UserHasAccessToDetailMixin, generic.UpdateView):
    model = User
    fields = ['username', 'picture', ]
    template_name = 'users/update_user.html'

    def get_success_url(self):
        return reverse_lazy('users:detail_user', args=[self.object.pk])
