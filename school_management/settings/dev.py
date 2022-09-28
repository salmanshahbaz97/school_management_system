from .common import *


DEBUG = True
SECRET_KEY = 'django-insecure-2ghmr%ud^drtax^pa&&sa(y)!msrcn_6q^c4m&@-wgrbf33!2c'

# for mysql database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'school_management_db',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'salman.123'
#     }
# }
# for postgres database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'school_management_system_db',
        'USER': 'postgres',
        'PASSWORD': '11223344',
        'PORT': 5433
    }
}
