"""Gunicorn *PRODUCTION* config file"""
from multiprocessing import cpu_count

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "backend.wsgi:application"
# The granularity of Error log outputs
loglevel = "info"
# The number of worker processes & threads for handling requests
workers = cpu_count() * 2 + 1
# The socket to bind
bind = "0.0.0.0:8000"
# Disable restarts on code changes
reload = False
# Write access and error info to /var/log
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = False
