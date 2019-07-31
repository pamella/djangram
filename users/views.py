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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_user = User.objects.get(pk=self.request.user.pk)
        follow_user = kwargs['object']
        context['request_user_has_followed'] = request_user.following.filter(pk=follow_user.pk).exists()

        return context


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


class UserFollowView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # User logado
        request_user = User.objects.get(pk=self.request.user.pk)
        # User que se quer seguir ou deixar de seguir
        follow_user = User.objects.get(pk=kwargs['pk'])
        # Checa se o user logado já segue o user que está interagindo
        request_user_has_followed = request_user.following.filter(pk=follow_user.pk).exists()

        if not request_user_has_followed:
            request_user.following.add(follow_user)
            follow_user.followers.add(request_user)
        else:
            request_user.following.remove(follow_user)
            follow_user.followers.remove(request_user)

        return reverse_lazy('users:detail_user', args=[follow_user.pk])