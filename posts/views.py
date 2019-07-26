from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from posts.forms import PostCreateForm
from posts.models import Post


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/list_post.html'
    ordering = ['-created_at', ]


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:list_post')

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def form_valid(self, form):
        # Mensagem estara disponivel no contexto do template
        # linkado acima em success_url
        messages.success(
            self.request,
            'Você compartilhou um novo post! Confira abaixo.'
        )
        return super().form_valid(form)
