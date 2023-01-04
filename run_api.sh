#!/bin/sh
sleep 10
su -m devops -c "python ./manage.py migrate" 
su -m devops -c "gunicorn --bind 0.0.0.0:9000 --workers 1 backend.wsgi:application"

