from .base import *

DEBUG = False

# TODO: Dejar solo el dominio de produccion
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'production-domain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # en caso de usar postgresql
        # ENGINE

        # en caso de unas mysql
        # ENGINE mysql


        # 'NAME': os.getenv('DB_NAME'),

        # 'USER': os.getenv('DB_USER'),

        # 'PASSWORD' : os.getenv('DB_PASWWORD'),

        # 'HOST': os.getenv(DB_HOST'),

        # 'PORT': os.getenv(DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'