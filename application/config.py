"""General Flask configuration."""
import os

class _BaseConfig(object):
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2
    # Enable protection against *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True
    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = 'dKRgIERpSvVZuxFXKceWjyrCqw3tvyhE'
    # Secret key for signing cookies and other things
    SECRET_KEY = 'Z30ojtSS6Ix9PspXRuqjSUFR0ocL5Zkt'

class ProductionConfig(_BaseConfig):
    DEBUG = False
    HOST_URL = 'https://mini-kep.herokuapp.com'
    DB = 'sqlite:////tmp/prod.db'

class DevelopmentConfig(_BaseConfig):
    DEBUG = True
    HOST_URL = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:123qwe@localhost/dev'
    DB = {
        'name': 'admin',
        'password': '123qwe',
        'dbname': 'dev',
        'host': 'localhost'}

class TestingConfig(_BaseConfig):
    DEBUG = True
    HOST_URL = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:123qwe@localhost/test'
    DB = {
        'name': 'admin',
        'password': '123qwe',
        'dbname': 'test',
        'host': 'localhost'
        }

