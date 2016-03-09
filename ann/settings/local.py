from ann.settings.base import *

SECRET_KEY = 'kl(1et7az7t-+(5^+z)yel36g*r+#be)kaev0sc#97%0=bx^l@'


DEBUG = True
INSTALLED_APPS += (
    #'debug_toolbar',  and other apps for local development
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