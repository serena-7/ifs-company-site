import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

FLASK_ENV = ENV = os.getenv('ENVIRONMENT')
if FLASK_ENV == "development":
    DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

PG_USER = os.getenv('DATABASE_USERNAME')
PG_PASS = os.getenv('DATABASE_PASSWORD')
PG_NAME = os.getenv('DATABASE_NAME')
PG_URL = os.getenv('DATABASE_URL')
PG_PORT = os.getenv('DATABASE_PORT')

SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASS}@{PG_URL}:{PG_PORT}/{PG_NAME}"

# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

# if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
#         "postgres://", "postgresql://", 1)
