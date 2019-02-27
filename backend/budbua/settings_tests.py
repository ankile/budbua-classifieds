from budbua.settings import *
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365)
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'budbuaTest',
        'Host': 'postgres',
        'User': 'runner',
        'Password': '',
        'Database': 'budbuaheaven',
        'PORT': '5432'

}
}
