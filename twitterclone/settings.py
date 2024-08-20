import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações básicas

SECRET_KEY = "django-insecure-lbc!nuc0koo9@e4o@f2%p=&y_)xv*wnqsppeqca+z096#f+-^o"
DEBUG = True
ALLOWED_HOSTS = []

# Configurações das aplicações

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "core",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "twitterclone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates/core'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "twitterclone.wsgi.application"

# Configuração do banco de dados

ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'seu_nome_de_banco_no_pythonanywhere',
            'USER': 'seu_usuario_do_pythonanywhere',
            'PASSWORD': 'sua_senha_do_pythonanywhere',
            'HOST': 'seu_host_do_pythonanywhere',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'twitter_clone_db',
            'USER': 'twitter_dev',
            'PASSWORD': 'twitter_dev',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Validação de senha

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internacionalização

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core/static']  # Ajustei para o diretório onde seus arquivos CSS estão localizados
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Diretório onde os arquivos estáticos serão coletados para produção

# Configurações adicionais

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
