#!/bin/bash
# Create local_settings.py from environment variables
set -x

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
LANGUAGE_CODE = 'en-nz'\n\
TIME_ZONE = 'Pacific/Auckland'\n\
MQ_FRAMEWORK = {\n\
    'HOST': '${MQHOST}',\n\
    'USER': '${MQUSER}',\n\
    'PASSWORD': '${MQPASSWORD}',\n\
    'EXCHANGE_PREFIX': 'notify.',\n\
    'HTTP_REST_CONTEXT': {\n\
        'SERVER_NAME': '${MQRESTSERVER}',\n\
        'SERVER_PORT': ${MQRESTPORT},\n\
        'SERVER_PROTOCOL': '${MQRESTPROTOCOL}',\n\
    }\n\
}\n" > ./utilities/local_settings.py
