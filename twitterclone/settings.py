import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações básicas

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', "django-insecure-lbc!nuc0koo9@e4o@f2%p=&y_)xv*wnqsppeqca+z096#f+-^o")
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['sumioshi.pythonanywhere.com', 'localhost', '127.0.0.1']

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
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Adicionado para servir arquivos estáticos em produção
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

# Configuração do banco de dados (somente MySQL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sumioshi$default',  # Nome do seu banco de dados
        'USER': 'sumioshi',  # Seu nome de usuário no PythonAnywhere
        'PASSWORD': 'MN^Trx6E@LQj',  # A senha do MySQL que você configurou no PythonAnywhere
        'HOST': 'sumioshi.mysql.pythonanywhere-services.com',
        'PORT': '3306',
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
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'core/static']

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Configurações adicionais

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
