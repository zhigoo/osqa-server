# encoding:utf-8
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    #level=logging.ERROR,
    level=logging.INFO,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)


DATABASE_NAME = 'osqa'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'               # Not used with sqlite3.
DATABASE_PASSWORD = 'zhigoo'               # Not used with sqlite3.
DATABASE_ENGINE = 'mysql'  #mysql, etc
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'

CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
APP_URL = 'http://ask.12stu.com'

#LOCALIZATIONS
TIME_ZONE = 'Asia/Shanghai'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'zh_CN'

DJANGO_VERSION = 1.1
OSQA_DEFAULT_SKIN = 'default'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges']
