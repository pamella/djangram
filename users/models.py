from django.contrib.auth.models import AbstractUser
from django.db import models


# Definindo um modelo de usuário personalizado
# https://docs.djangoproject.com/pt-br/2.2/topics/auth/customizing/#specifying-a-custom-user-model
# https://docs.djangoproject.com/pt-br/2.2/topics/auth/customizing/#extending-django-s-default-user

# Many to many field
# https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/
class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField('Imagem de perfil', default='/img/userpicture.jpeg')
    following = models.ManyToManyField('self', verbose_name='Seguingo',
        related_name='following_users', blank=True, symmetrical=False)
    followers = models.ManyToManyField('self', verbose_name='Seguidores',
        related_name='followers_users', blank=True, symmetrical=False)
    created_at = models.DateTimeField(auto_now_add=True)
