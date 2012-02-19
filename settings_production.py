#coding: utf-8
# Django settings for myblog project.
import os
rel=lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)),*x)#处理静态文件之用
STATIC_PATH=rel('static')#处理静态文件之用

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('******', '******@gmail.com'),
)

MANAGERS = ADMINS

AKISMET_API_KEY = '7f553d6a2e2e'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '******',                      # Or path to database file if using sqlite3.
        'USER': '******',                      # Not used with sqlite3.
        'PASSWORD': '******',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/username/webapps/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://domain/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = 'http://pynotes.info/static/admin/'
ADMIN_MEDIA_PREFIX = 'http://domain/static/grappelli/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tmumo117rt=ya1-wydb*#@zwr*bzxlj-k)@gntpd-2e04h9@%&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'myblog.http.SetRemoteAddrFromForwardedFor',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'myblog.urls_production'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel('templates'),
    #os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'captcha',
    'tinymce',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'myblog.blog',
    'django.contrib.comments',
)

TINYMCE_JS_URL=MEDIA_URL+'tiny_mce/tiny_mce_src.js'
TINYMCE_JS_ROOT=MEDIA_ROOT+'tiny_mce/'
TINYMCE_DEFAULT_CONFIG = {
'theme': "advanced",
'plugins': "syntaxhl",
'theme_advanced_buttons2_add': "|,syntaxhl",
'theme_advanced_toolbar_location' : "top",
'theme_advanced_toolbar_align' : "left",
'width': 600,
'height': 400,
}

TEMPLATE_CONTEXT_PROCESSORS = (
   "django.contrib.auth.context_processors.auth",
   "django.core.context_processors.request",
   "django.core.context_processors.i18n",
   'django.contrib.messages.context_processors.messages',
)
GRAPPELLI_INDEX_DASHBOARD = 'myblog.dashboard.CustomIndexDashboard'

FILEBROWSER_URL_FILEBROWSER_MEDIA =MEDIA_URL+'filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA =MEDIA_ROOT +'filebrowser/'
FILEBROWSER_DIRECTORY =MEDIA_ROOT +'uploads/'

CACHE_BACKEND='db://my_cache_table'

EMAIL_HOST='smtp.webfaction.com'
EMAIL_HOST_PASSWORD='******'
EMAIL_HOST_USER='******'
DEFAULT_FROM_EMAIL ='**@domain'
SERVER_EMAIL ='**@domain'
EMAIL_PORT=587
EMAIL_USE_TLS=True
