#!/bin/sh
# Authentication migration must run first in newer versions of Django
python manage.py migrate auth --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input

# Run crawler immediatelly
python manage.py scrapy > /var/log/crawler.log
# Setup a cron job for crawling
crontab -l | { cat; echo "*/10 * * * * /usr/local/bin/python /project/manage.py scrapy > /var/log/crawler.log 2>&1"; } | crontab -

/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
