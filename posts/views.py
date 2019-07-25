from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy

from posts.models import Post
from posts.forms import PostCreateForm


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/list_post.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:list_post')

    def get_initial(self):
        return {
            'user': self.request.user,
        }