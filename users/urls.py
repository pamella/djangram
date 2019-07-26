from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('perfil/<int:pk>/', UserDetailView.as_view(), name='detail_user'),

]
