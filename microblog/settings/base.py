"""
Django settings for microblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ------------------------VIDEO SNIPT----------------
# This is his snippet of code for setting up absolute paths in django
# import os # Done elsewhere in this file
# import os # Already required above
# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
# ----------------------------------


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1k+kyzk+)40)chk16=#a00i2v*3mh5eut8rzc9gtvf&4*v^ry='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# -------------------VIDEO----------------
# He talks about this...i should have listened
ALLOWED_HOSTS = []

# People who get e
# Names and email addresses that are considered to be admins capable of
# dealing with site problems - get email when site throws a 500
ADMINS = (
    ("Mohammad Abdeljalil", "msabdeljalil@gmail.com")
)

# Used whenever the mail_managers() method is called
MANAGERS = ADMINS
# Application definition

# -------------/VIDEO--------------------
# All of these apps contain a models.py  file, since that is what
# distinguishes a python module from a jango app
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # YOu can disable the admin app by commenting out line below
    'django.contrib.admin',
    # Y0u can disable the admindoocs app by commenting out line below
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = ()

LOCAL_APPS = ()

# The tutorial remaned the original installed_apps to DJANGO_APPS,
# added THIRD_PARTY_APPS and LOCAL_APPS, and the concated them here
# This makes testing easier cuz we can tell test runner to only
# test apps listed in LOCAL_APPS, not any of the others
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# These are "in the middle" of a response in that they are run before
# *and* after the view fucntions:
# - When exectued *before* the view (on a request) they are read top to bottom
# - When exectued *after* the view (on a response) they are read bottom to top
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Tells D which module to use *first* when building URL patterns
ROOT_URLCONF = 'microblog.urls'

# Python dotted oath to the WSGI app used by d's 'runserver'
# Luckily, the one that django provides will work for both local dev &
# the final server, and it's already been set, so we just leave it alone
WSGI_APPLICATION = 'microblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url
# DATABASES = {'default': dj_database_url.config()}
DATABASES['default'] = dj_database_url.config()  # From StackOverflow

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

# If False, D will make some optimizations so as not to load
# internationalization machinery
USE_I18N = True

# if False, D will not format dates, numbers, and calednars
# according to the current locale
USE_L10N = True

# If false, D will not use timezone-aware datetimes (user timezone that is).
USE_TZ = True


# ---------------FROM VIDEO (OLD?) ------------------
# Absolute File system path to the directory that will hold user-uploaded files
# Ex: "/home/media/media.alwrence.com/media/"
MEDIA_ROOT = root("..", "uploads")

# URL that handles the media served from MEDIA_ROOT. MAKE
# sure to end this path with a slash.
# Ex: "http://media.lawrence.com/static", "http://example.com/media/"
MEDIA_URL = ""

# Absolute path to dir where static assets files in project are stored
# Do't put anything in this dir urself; store ur static files
# in the apps' "/static/" subdir and in STATICFILES_DIRS
# EX: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = root("..", "static")

#     ----------------Present outside of video------------
# Url prefix for Static files (CSS, JavaScript, Images)
# Needs to end in a slash
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
#     ----------------/Present-----------------------------

# Additional locations of static files.
# You typically only have one of these, but you might be running
# an app alongside an exisitng site built in another language
# or framework, you could list that sites/apps static files here
# and D would hav access to them as well.
STATICFILES_DIRS = (
    # Put stings here, like "/home/html/static" or "c:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute not relative paths
    root("assets"),
)

# While STATICFILES_DIRS searches 'where', this searches 'how'
STATICFILES_FINDERS = (
    # Defualt: search on the filesystem where u specified the static files to b
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # Then it searches for a file named static inside of each app's directory
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Works just like staticfiles_finder but for finding templates, not assets
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)


# Works like STATICFILES_DIRS - it tells D where to look for template files
# that are not inside of an app
# This is where a person generally expects to find your site-wide templates
# and layouts for a specific app
TEMPLATE_DIRS = (
    # Put stings here, like "/home/html/static" or "c:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute not relative paths
    root("..", "templates"),
)

# Also some stuff on loggers that I was too lazy to copy over...
# ------------------- END VIDEO STUFF ------------
