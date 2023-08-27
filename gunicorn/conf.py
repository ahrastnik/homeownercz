"""Gunicorn *DEVELOPMENT* config file"""
# NOTE: DON'T RUN GUNICORN DIRECTLY! Instead, run it in a Docker container
from multiprocessing import cpu_count

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "backend.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes & threads for handling requests
workers = cpu_count() * 2 + 1
#threads = 4 # TODO: Figure out the best thread/worker ratio
# The socket to bind
bind = "0.0.0.0:8080"
# Restart workers when code changes (development only!)
reload = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = False
