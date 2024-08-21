import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-&34da0j5b8g(cwlaka)_3#znp1rz)!ub$2rnra20v73zdc!@3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'allauth',
    'rest_framework',
    'rest_framework_simplejwt',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'corsheaders',
    'users',
    'mileage',
    'payments',
    'store',
    'reviews',
    'cash'
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'path.to.CustomTokenSerializer',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 이 줄을 두 번째에 두어야 합니다.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 사용자 모델에서 username 필드를 사용하지 않도록 설정
ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # username 필드를 사용하지 않음
ACCOUNT_USERNAME_REQUIRED = False  # username을 요구하지 않음
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # 이메일로 인증
ACCOUNT_EMAIL_REQUIRED = True  # 이메일 필수
ACCOUNT_UNIQUE_EMAIL = True  # 이메일 고유성 유지

ROOT_URLCONF = 'oasis_api.urls'

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

WSGI_APPLICATION = 'oasis_api.wsgi.application'

AUTH_USER_MODEL = 'users.CustomUser'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'

CORS_ALLOW_ALL_ORIGINS = True

CORS_EXPOSE_HEADERS = ['Content-Type', 'Authorization']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # 사용하려는 SMTP 서버 주소
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'angele0709@naver.com'  # 발송할 이메일 주소
EMAIL_HOST_PASSWORD = 'tlsgptj0709!'  # 이메일 계정 비밀번호
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATIC_URL = '/static/'