## Graphite local_settings.py
# Edit this file to customize the default Graphite webapp settings
#
# Additional customizations to Django settings can be added to this file as well

from os import getenv, urandom

SECRET_KEY = getenv('SECRET_KEY', urandom(24).encode('hex'))

if getenv("CLUSTER_SERVERS"):
    CLUSTER_SERVERS = getenv("CLUSTER_SERVERS").split(',')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'graphite': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

try:
    from graphite.custom_settings import *
except ImportError:
    pass