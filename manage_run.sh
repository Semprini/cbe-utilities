#!/bin/sh
# Create local_settings.py from environment variables
echo -e "import os\n\
from utilities.settings import BASE_DIR\n\n\
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\
DATABASES = {\n\
    'default': {\n\
        'ENGINE': 'django.db.backends.${DBENGINE}',\n\
        'NAME': '${DBNAME}',\n\
        'HOST': '${DBHOST}',\n\
        'PORT': ${DBPORT},\n\
        'USER': '${DBUSER}',\n\
        'PASSWORD': '${DBPASSWORD}',\n\
    }\n\
}\n\
MQ_FRAMEWORK = {\n\
    'HOST': '${MQHOST}',\n\
    'USER': '${MQUSER}',\n\
    'PASSWORD': '${MQPASSWORD}',\n\
    'EXCHANGE_PREFIX': 'notify.',\n\
    'HTTP_REST_CONTEXT': {\n\
        'SERVER_NAME': '${MQRESTSERVER}',\n\
        'SERVER_PORT': ${MQRESTPORT},\n\
        'SERVER_PROTOCOL': ${MQRESTPROTOCOL},\n\
    }\n\
}\n" > /code/utilities/local_settings.py

sleep 10
python manage.py migrate
python manage.py getorcreatesuperuser ${SUNAME} ${SUEMAIL} ${SUPASS}
python manage.py runserver 0.0.0.0:8000
