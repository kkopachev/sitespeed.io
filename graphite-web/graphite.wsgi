from os import environ
from subprocess import call
from sys import argv

from django.core.wsgi import get_wsgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphite.settings')

# call(['django-admin.py', 'syncdb', '--noinput'])
call(['django-admin.py', 'migrate', '--run-syncdb'])

application = get_wsgi_application()

# Build search index
call('/opt/graphite/bin/build-index.sh')