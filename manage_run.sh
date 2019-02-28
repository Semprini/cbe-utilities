#!/bin/sh

# Create local_settings.py from environment variables
bash -c /code/create_local_settings.sh

sleep 10
python manage.py migrate
python manage.py getorcreatesuperuser ${SUNAME} ${SUEMAIL} ${SUPASS}
python manage.py runserver 0.0.0.0:8000
