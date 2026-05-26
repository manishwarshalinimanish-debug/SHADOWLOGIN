import os
import smtplib
from email.mime.text import MIMEText


def sound_alert():

    print("ALERT SOUND")


def send_email_alert(log):

    sender_email = os.environ.get("EMAIL_USER")

    sender_password = os.environ.get("EMAIL_PASS")

    receiver_email = sender_email

    subject = "ShadowLogin Attack Alert"

    body = f"""
Attack Detected

IP: {log['ip']}
Username: {log['username']}
Password: {log['password']}
Attempts: {log['attempts']}
Country: {log['country']}
Region: {log['region']}
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:

        print("Connecting to Gmail SMTP...")

        server = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            timeout=10
        )

        print("Logging into Gmail...")

        server.login(
            sender_email,
            sender_password
        )

        print("Sending email...")

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("EMAIL SENT SUCCESSFULLY")

    except Exception as e:

        print("EMAIL ERROR:", e)
