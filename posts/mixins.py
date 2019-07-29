from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from posts.models import Post


class UserHasAccessToDeletePostMixin(LoginRequiredMixin):
    '''
        Esse mixin evita que um user delete um post
        que ele não seja o autor.
    '''

    def handle_no_permission(self):
        messages.error(
            self.request,
            'Você não pode deletar um post de outro usuário!',
        )
        return redirect('posts:list_post')

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])

        if not post.author == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
