from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from users.models import User


# Django Mixins
# https://docs.djangoproject.com/en/2.2/topics/class-based-views/mixins/#
# http://ccbv.co.uk/projects/Django/2.2/django.contrib.auth.mixins/

class UserHasAccessToDetailMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        # mostrando mensagens
        messages.error(
            self.request,
            'Você não pode editar um perfil que não é seu!'
        )
        return redirect('users:logout_user')

    def dispatch(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        # Pegando o pk do user a ser editado (vem da url do browser)
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)

        if not user == request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)
