# src/config/keylogger_config.py
import configparser

class Config:
    """Class to handle configuration settings."""
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../config/config.ini')
        self.email_address = self.config['DEFAULT']['EmailAddress']
        self.recipient_email_address = self.config['DEFAULT']['RecipientEmailAddress']
        self.email_password = self.config['DEFAULT']['EmailPassword']
        self.save_report_every = int(self.config['DEFAULT']['SaveReportEvery'])