#!/bin/bash

pg_host="$1"
pg_port="$2"
timeout="$3"

until nc -w $timeout -z $pg_host $pg_port; do
    echo "Connection to ${pg_host}:${pg_port} was failed"
    sleep 1
done

python2.7 manage.py migrate
python2.7 manage.py runserver 0.0.0.0:8000

