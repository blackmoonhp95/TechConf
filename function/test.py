import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

POSTGRES_URL = 'mypostserver.postgres.database.azure.com' 
POSTGRES_USER = 'useracc@mypostserver' 
POSTGRES_PW = 'Maiyeuem@hp95' 
POSTGRES_DB = 'techconfdb' 

print(POSTGRES_DB, POSTGRES_USER, POSTGRES_PW, POSTGRES_URL)

connection = psycopg2.connect(dbname=POSTGRES_DB,
                                user=POSTGRES_USER,
                                password=POSTGRES_PW,
                                host=POSTGRES_URL)

attendees = connection.execute()
