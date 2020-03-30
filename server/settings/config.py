import os
from . import confsec


DEBUG = confsec.DEBUG
JOB_TOKEN = confsec.JOB_TOKEN

APP_DIR = os.getcwd()

GOG_API_URL = confsec.GOG_API_URL
GOG_API_COOKIES = confsec.GOG_API_COOKIES
GOG_JSON_PATH = os.path.join(APP_DIR, 'gog.json')
GOG_JSON_PARSED_PATH = os.path.join(APP_DIR, 'gog_parsed.json')

PUBLIC_DIR = os.path.join(APP_DIR, 'public')
STATIC_DIR = os.path.join(PUBLIC_DIR, 'static')
