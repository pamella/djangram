from django.urls import path

from users.views import (UserDetailView, UserLoginView, UserLogoutView,
                         UserSignupView, UserUpdateView, UserFollowView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('perfil/<int:pk>/', UserDetailView.as_view(), name='detail_user'),
    path('signup/', UserSignupView.as_view(), name='signup_user'),
    path('perfil/<int:pk>/editar/', UserUpdateView.as_view(), name='update_user'),
    path('seguir/<int:pk>/', UserFollowView.as_view(), name='follow_user'),

]
