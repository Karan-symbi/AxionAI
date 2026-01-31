import pandas as pd
import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class Schedule:
    def __init__(self):
        self.server = "smtp.gmail.com"
        self.port = 587
        self.sender = "axionai101@gmail.com"
        self.password = os.getenv("app_password")

    def defaults(self,start_date,start_time,slot_length):
        self.date = start_date
        self.time = start_time
        self.slot_length = slot_length
    
    def schedule_slots(self, file_path):
        self.df = pd.read_csv(file_path)

        # Combine date and time into datetime object
        start_datetime = datetime.strptime(
            f"{self.date} {self.time}", "%Y-%m-%d %H:%M"
        )

        slots = []

        for i in range(len(self.df)):
            slot_start = start_datetime + timedelta(minutes=i * self.slot_length)
            slot_end = slot_start + timedelta(minutes=self.slot_length)

            slot_str = f"{slot_start.strftime('%Y-%m-%d %H:%M')} - {slot_end.strftime('%H:%M')}"
            slots.append(slot_str)

        self.df["Slot"] = slots


    def send_emails(self):
        names = self.df["Name"]
        emails = self.df["Email"]
        slots = self.df["Slot"]
        for name,email,slot in zip(names,emails,slots):
            message = MIMEMultipart("alternative")
            message["Subject"] = "Interview Invitation – First Round Cleared"
            message["From"] = self.sender
            message["To"] = email
            html = f"""
    <html>
        <body>
            <p>
                    Dear {name},<br><br>
                    We are pleased to inform you that you have successfully cleared the first round of the interview process.<br><br>

                    You are hereby invited to attend the next round of interviews, scheduled as per the details below:<br><br>

                    <strong>Date:</strong> {self.date}<br>
                    <strong>Time:</strong> {slot}<br>

                    Please ensure that you are available and join the interview on time. Further instructions, if any, will be shared with you prior to the interview.<br><br>

                    We wish you the very best and look forward to speaking with you.<br><br>

                    Best regards,<br>
                    <strong>Hiring Team</strong>
                </p>

              </body>
            </html>
            """
            part = MIMEText(html, "html")
            message.attach(part)
            context = ssl.create_default_context()
            with smtplib.SMTP(self.server, self.port) as server:
                server.starttls(context=context)
                server.login(self.sender, self.password)
                server.sendmail(self.sender, email, message.as_string())


