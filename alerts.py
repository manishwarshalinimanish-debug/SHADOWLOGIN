import smtplib
from email.mime.text import MIMEText


def sound_alert():

    print("ALERT SOUND")


def send_email_alert(log):

    sender_email = "manishwarshalinimanish@gmail.com"

    sender_password = "clus absd cwhh ihjx"

    receiver_email = "manishwarshalinimanish@gmail.com"

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

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=5
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("Email Alert Sent Successfully")

    except Exception as e:

        print("Email Error:", e)
