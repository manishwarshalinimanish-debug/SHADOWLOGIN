import os
import smtplib
from email.mime.text import MIMEText

def sound_alert():

    os.system("echo '\a'")

def send_email_alert(log):

    sender_email = "manishwarshalinimanish@gmail.com"
    sender_password = "clus absd cwhh ihjx"

    receiver_email = "YOUR_EMAIL@gmail.com"

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

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()

        print("Email Alert Sent")

    except Exception as e:
        print("Email Error:", e)
