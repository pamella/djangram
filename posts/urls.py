from django.urls import path

from posts.views import PostListView, PostCreateView

app_name = 'posts'

urlpatterns = [
    path('lista_posts/', PostListView.as_view(), name='list_post'),
    path('postar/', PostCreateView.as_view(), name='create_post'),
]
