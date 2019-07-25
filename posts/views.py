from django.shortcuts import render
from django.views import generic

from posts.models import Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/list_post.html'
