from decouple import config
import django_heroku  # Configure Django App for Heroku.

from djangram.settings.base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '.herokuapp.com',
]

# social_django
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',

    # django
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# ID do cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '129312100772-cg9kup64i6vkhq99om9nqcqr48ogq4eo.apps.googleusercontent.com'
# Chave secreta do cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Hi0lpz-1jtLb6rTYlVskMidC'

# Instagram
# https://www.instagram.com/developer/authentication/


# Email
EMAIL_HOST_USER = 'testedjangojr@gmail.com'
EMAIL_HOST_PASSWORD = 'senhaTEST'


django_heroku.settings(locals())
