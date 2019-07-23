from django.db import models
from django.contrib.auth.models import User


# Django fields
# https://docs.djangoproject.com/en/2.2/ref/models/fields/

# on_delete
# https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete

# class Meta
# https://docs.djangoproject.com/en/2.2/ref/models/options

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagem', upload_to='posts/')
    description = models.CharField(max_length=256, verbose_name='Descrição')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='Modificado em', auto_now=True)

    def __str__(self):
        return f'Post {self.id} | Author {self.author} | Created at {self.created_at}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
