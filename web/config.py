import os

basedir = os.path.abspath("")


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = 'mypostserver.postgres.database.azure.com'
    POSTGRES_USER = "useracc@mypostserver"
    POSTGRES_PW = "Maiyeuem@hp95"
    POSTGRES_DB = "techconfdb"
    DB_URL = "postgresql://{user}:{pw}@{url}/{db}".format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
    )
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = "LWd2tzlprdGHCIPHTd4tp5SBFgDszm"
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://techconf-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=YD/j35ry932hGKdjTNBvf8jGUe39w1JyxnmA7eTiFHs='
    SERVICE_BUS_QUEUE_NAME = "notificationqueue"
    ADMIN_EMAIL_ADDRESS = "info@techconf.com"
    SENDGRID_API_KEY = ""  # Configuration not required, required SendGrid Account

    # for local host if Azure functions served locally
    # API_URL = "http://localhost:7071/api"
    API_URL = "https://sendfunction.azurewebsites.net/api"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
