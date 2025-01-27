import json
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('EMAIL_USER') 
SENDER_PASSWORD = os.getenv('EMAIL_PASS') 

def send_email(receiver_email, subject, body_text):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            message = f"Subject: {subject}\n\n{body_text}"

            server.sendmail(SENDER_EMAIL, receiver_email, message)

            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_email_api(event, context):
    try:
        body = json.loads(event['body'])
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        if not receiver_email or not subject or not body_text:
            return {"statusCode": 400, "body": json.dumps({"message":"Missing required fields"})}
        
        email_sent = send_email(receiver_email, subject, body_text)

        if email_sent:
            return {"statusCode": 200, "body":json.dumps({"message":"Email sent sucessfully"})}
        else:
            return { "statusCode": 500, "body": json.dumps({"message":"Failed to send email"})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"message": "Internal server error", "error": str(e)})}
    