from django.contrib.auth.forms import UserCreationForm

from users.models import User


# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]