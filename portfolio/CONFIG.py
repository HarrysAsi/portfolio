import os

IS_SERVER = False
DEBUG = True

# Application Information
SECRET_KEY = 'nk^axnq1$k2_c5uh7k3bq+cigv^rxm@-p-js2y#dp5a#jt))3q'

# Gmail configuration settings
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", None)

# Regex for the domain
DOMAIN_REGEX = "xarhsasi.systems"

# Database information
if not IS_SERVER:
    DATABASE_NAME = 'portfolio'
    USER = 'root'
    PASSWORD = ''
    HOST = ''
    DATABASE_PORT = ''
else:
    DATABASE_NAME = os.environ.get("DATABASE_NAME_PORTFOLIO", None)
    USER = os.environ.get("DATABASE_USER_PORTFOLIO", None)
    PASSWORD = os.environ.get("DATABASE_PASSWORD_PORTFOLIO", None)
    HOST = os.environ.get("DATABASE_HOST_PORTFOLIO", None)
    DATABASE_PORT = os.environ.get("DATABASE_PORT_PORTFOLIO", None)
