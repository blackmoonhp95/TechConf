from azure.servicebus import ServiceBusClient
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.BaseConfig")

app.secret_key = app.config.get("SECRET_KEY")


servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=app.config.get("SERVICE_BUS_CONNECTION_STRING"),
    logging_enable=True,
)

db = SQLAlchemy(app)

from . import routes
