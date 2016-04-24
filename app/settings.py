import os

class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ERROR_LOG_PATH=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))#os.path.dirname(os.path.realpath(__file__))
    HOST='0.0.0.0'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    CELERY_BROKER_URL = 'redis://33.33.33.10:6379/0'
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'

    # This allows us to test the forms from WTForm
    WTF_CSRF_ENABLED = False

config = {
    'development': DevConfig,
    'production': ProdConfig,


    'default': DevConfig
}
