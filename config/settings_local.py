# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k2sq98o4ya$b&#rl%-_i13n^p4sw$%-eo19tt4i$lz#ex4&c9f'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 't_django',
        'USER': 'gabe',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}