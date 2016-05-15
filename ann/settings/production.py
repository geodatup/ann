from ann.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kl(1et7az7t-+(5^+z)yel36g*r+#be)kaev0sc#97%0=bx^l@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'gunicorn', # other apps for production site
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}
