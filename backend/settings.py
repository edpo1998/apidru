"""
    Archivo de Configuracion 
        El presente archivo esta destinado para la configuracion en el
        ambiente de produccion cargando cada una de las customizaciones
        y variables de mayor incidencia en el proyecto.
    Fecha Actualizacion: 03/01/2023 
    Author: Erick Poron
"""

# Python
import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

# Construccion de las rutas del proyecto: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+tnqb6d7qq@xeq_k&33j5fsy85d9jakt=km1k3x(9z43wl+1k3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DJANGO_LOG_LEVEL = DEBUG 

# Configuraciones de Decodificacion, Zona Horaria e Idioma
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10B = True
USE_TZ = True


# Configuracion de Cors
ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:3000"
#]

WSGI_APPLICATION = 'backend.wsgi.application'

ROOT_URLCONF = 'backend.urls'

# Definicion de aplicaciones del proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    "corsheaders",
    "api"
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Configuracion de contrasenias
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configuraciones del Usuario customizado
AUTH_USER_MODEL = 'api.Usuario'

# Configuraciones de los archivos estaticos
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuraciones del LOGGER
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  #
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'logfile': {
            'class':'logging.FileHandler',
            'formatter': 'standard',
            'filename':f'{LOGS_DIR}/logsfile' ,
        },
    },
    'loggers': {
        '': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
    'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

#Configuraciones del Token JWT 
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    ####### Cookie
    'AUTH_COOKIE': 'access_token',  
    'AUTH_COOKIE_DOMAIN': None,    
    'AUTH_COOKIE_SECURE': True,    # Whether the auth cookies should be secure (https:// only).
    'AUTH_COOKIE_HTTP_ONLY' : True,
    'AUTH_COOKIE_PATH': '/',        
    'AUTH_COOKIE_SAMESITE': 'None', 
}

# Configuraciones del DRF para la APIREST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication', 
        'rest_framework.authentication.SessionAuthentication',
        #'api.authentication.MyOwnTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

load_dotenv()
# DATABASE
host_postgresql = os.getenv('POSTGRESQL_HOST')
name_postgresql = os.getenv('POSTGRESQL_NAME')
port_postgresql = os.getenv('POSTGRESQL_PORT')
user_postgresql = os.getenv('POSTGRESQL_USER')
pwd_postgresql = os.getenv('POSTGRESQL_PWD')
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': name_postgresql,
        'USER': user_postgresql,
        'PASSWORD': pwd_postgresql,
        'HOST': host_postgresql,
        'PORT': port_postgresql
    }
}

# API CONFIGURATION 
URL_SERVICE = os.getenv('URL_SERVICE')
KEY_API = os.getenv('KEY_API')
VERSION_API = os.getenv('VERSION_API')

# Configuracion en entorno de Pruebas
try:
    from .local_settings import *
except ImportError:
    pass
