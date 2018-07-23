#!/bin/bash
python2.7 manage.py migrate
python2.7 manage.py runserver 0.0.0.0:8000

