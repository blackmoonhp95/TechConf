import logging
from urllib import response
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content
import traceback


api_key = os.getenv("SENDGRID_API_KEY")
sg = SendGridAPIClient(api_key=api_key)
from_email = "quangnmbk58@outlook.com.vn"


def main(msg: func.ServiceBusMessage):

    try:
        notification_id = int(msg.get_body().decode('utf-8'))
        logging.info('Python ServiceBus queue trigger processed message: %s', notification_id)
        
        connect = psycopg2.connect(dbname="techconfdb",
                                user="useracc@mypostserver",
                                password="Maiyeuem@hp95",
                                host="mypostserver.postgres.database.azure.com")

    
        with connect.cursor() as cur:
            cur.execute("SELECT message, subject FROM notification WHERE id = {}".format(notification_id))
            notification = cur.fetchone()
            cur.execute("SELECT first_name, email FROM attendee")
            attendees = cur.fetchall()
            
            logging.info(notification)
            logging.info(attendees)
        
            for attendee in attendees:
                to_email = attendee[1]
                subject = notification[1]
                content = Content("text/plain", notification[0])
                mail = Mail(from_email, to_email, subject, content)
                response = sg.send(mail)

            cur.execute("UPDATE notification \
                        SET \
                            status = 'Notified {} attendees', \
                            completed_date =  NOW() \
                        WHERE id = {}".format(len(attendees), 
                                            notification_id))

    except Exception as error:
        logging.error(traceback.format_exc())
        return func.HttpResponse(traceback.format_exc())
    finally:
        connect.commit()
        connect.close()
    
    