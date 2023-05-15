from os import getenv
from dotenv import load_dotenv
from  distutils.util import strtobool


load_dotenv()


class Config(object):
    MONGO_PORT = int(getenv('CARDIO_MONGO_PORT', default=27017))
    MONGO_HOST = getenv('CARDIO_MONGO_HOST', default='localhost')
    MONGO_DB_NAME = getenv('CARDIO_MONGO_DB_NAME', default='cardio')

    SECRET_KEY = getenv('CARDIO_SECRET_KEY', default='secret_key')
    PORT = int(getenv('CARDIO_PORT', default=80))
    DEBUG = strtobool(getenv('CARDIO_DEBUG', default='False'))
