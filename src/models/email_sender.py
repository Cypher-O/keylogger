# src/models/email_sender.py
import smtplib
import configparser
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../config/config.ini') 
        self.email_address = self.config['DEFAULT']['EmailAddress']
        self.recipient_email_address = self.config['DEFAULT']['RecipientEmailAddress']
        self.email_password = self.config['DEFAULT']['EmailPassword']

    def prepare_mail(self, subject, body, attachment=None):
        """Prepare the email content."""
        msg = MIMEMultipart()
        msg["From"] = self.email_address
        msg["To"] = self.recipient_email_address 
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Attach the file if provided
        if attachment:
            with open(attachment, "rb") as att:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(att.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={attachment.split('/')[-1]}",
                )
                msg.attach(part)

        return msg.as_string()

    def send_email(self, to_email, subject, body, attachment=None):
        """Send an email with the given message."""
        msg = self.prepare_mail(subject, body, attachment)
        try:
            # with smtplib.SMTP(host="smtp.office365.com", port=587) as server:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.sendmail(self.email_address, to_email, msg)
                print('Email sent successfully!')
                logging.info('Email sent successfully!')
        except smtplib.SMTPException as e:
            print(f'SMTP error: {e}')  
        except Exception as e:
            print(f'Failed to send email: {e}')
