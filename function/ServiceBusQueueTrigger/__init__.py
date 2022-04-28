import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s', notification_id)
    
    connect = psycopg2.connect(dbname="techconfdb",
                               user="useracc@mypostserver",
                               password="Maiyeuem@hp95",
                               host="mypostserver.postgres.database.azure.com")

    print("hello world!")

    try:
        pass
        with connect.cursor() as cur:
            noti_table = cur.execute("SELECT message, subject FROM notification WHERE id = {}".format(notification_id))
            att_table = cur.execute("SELECT first_name, email FROM attendee")
            
            print(len(noti_table), type(noti_table))
            
            
        # TODO: Get notification message and subject from database using the notification_id

        # TODO: Get attendees email and name

        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified

    except Exception as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        pass