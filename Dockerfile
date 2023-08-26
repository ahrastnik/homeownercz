FROM python:3.8.17-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install all required packages
RUN apt-get update && apt-get install -y cron supervisor

# Install all required Python packages
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium

# Setup Django Environment
COPY ./backend /project
WORKDIR /project

# Configure supervisor
COPY supervisord.conf /etc/supervisor/supervisord.conf
# Setup a cron job for crawling
RUN crontab -l | { cat; echo "* * * * * /usr/local/bin/python /project/manage.py scrapy > /var/log/crawler.log 2>&1"; } | crontab -
# Run supervisor which will control both Django and crawling
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
