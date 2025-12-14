import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()   # 🔥 THIS LINE WAS MISSING

class BulkMessenger:

    def __init__(self, message, emails: list[str]):
        self.msg = message
        self.mails = emails

    def sending(self):
        sender_email = os.getenv("SENDER_EMAIL")
        app_password = os.getenv("EMAIL_APP_PASSWORD")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        for mail in self.mails:
            msg = MIMEText(self.msg)
            msg["From"] = sender_email
            msg["To"] = mail
            msg["Subject"] = "Bulk Message"

            server.sendmail(sender_email, mail, msg.as_string())
            print(f"Sent email to {mail}")

        server.quit()