
from pathlib import Path
from django.shortcuts import render
import os
import DistribuidoraOccidentalPy.db as db


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^3bidr4)ckdv*vlpvv$nw=!ee!w7of-3p2rmez-ut1yf7$&zjg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'carrito',
    'usuario',
    'import_export',
    'correo',
    'direcciones',
    'orden',
    'inventario',
]

# Jazmine Setings

JAZZMIN_SETTINGS = {
    "site_title": "Distribuidora Occidental",
    "site_header": "Distribuidora Occidental",
    "site_brand": "Distribuidora Occ",
    "site_logo": "/img/logo.png",
    "site_icon": "/img/logo.png",
    "site_logo_classes": "img-none shadow-none",
    "welcome_sing": "Bienvendo a Distribuidora Occidental",
    "copyright": "Distribuidora Occidental copyright",
    "show_sidebar": True,
    "navigation-expanded": False,
    "search-model": "auth.User",
    "search_model": ["auth.User"],
    "hide-apps": [
        
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "accounts": "fas fa-user-circle",
        "accounts.Account": "user-circle",
        "Marca": "fas fa-user-circle",

        
        
    },
    "related-modal-active": False,
    "show_ui_builder": False,
    "changeform_format": "carrousel",
    "changeform_format_overrides": {"auth.user": "vertical_tabs","auth.group":"vertical_tabs"},
    "custom-css": "css/dashboard/admin.css",
    
    "topmenu_links": [
        {"name": "Inicio",  "url": "index", "permissions": ["auth.view_user"]},
    ]
    
    
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "united",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DistribuidoraOccidentalPy.urls'

AUTH_USER_MODEL = 'usuario.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'DistribuidoraOccidentalPy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = db.MYSQL


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL ='media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#variables
LOGOUT_REDIRECT_URL ="login"

##Variables para el Correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True
EMAIL_PORT = 465
