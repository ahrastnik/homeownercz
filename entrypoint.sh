#!/bin/sh
# Authentication migration must run first in newer versions of Django
python manage.py migrate auth --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input

/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
