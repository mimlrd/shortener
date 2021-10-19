#!/bin/sh
# this script is used to boot a Docker container
#source venv/bin/activate
export FLASK_ENV=$FLASK_ENV
while true; do
    if [ "$?" = "0" ]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn --worker-class gevent --workers 3 --bind 0.0.0.0:5050 app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info