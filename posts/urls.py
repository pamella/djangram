from django.urls import path

from posts.views import (PostCreateView, PostDeleteView, PostDetailView,
                         PostListView)

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list_post'),
    path('postar/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('deletar/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),

]
