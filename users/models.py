from django.contrib.auth.models import AbstractUser
from django.db import models


# Definindo um modelo de usuário personalizado
# https://docs.djangoproject.com/pt-br/2.2/topics/auth/customizing/#specifying-a-custom-user-model
# https://docs.djangoproject.com/pt-br/2.2/topics/auth/customizing/#extending-django-s-default-user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField('Imagem de perfil', default='/img/userpicture.jpeg')
    created_at = models.DateTimeField(auto_now_add=True)
