#!/bin/bash

virtualenv --python=python3.6 env

echo '----------------------------------MADE VIRTUALENV----------------------------------'


. env/bin/activate

echo '--------------------------------ACTIVATED VIRTUALENV-------------------------------'

pip install -r requirements/base.txt

echo '-------------------------------INSTALLED REQUIREMENTS------------------------------'

. env.sh

echo '--------------------------------SOURCED ENVIRONMENT---------------------------------'

echo '-----------------------------STARTING THE be APPLICATION---------------------------'

python manage.py runserver
