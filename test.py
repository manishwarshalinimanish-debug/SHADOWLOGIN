import smtplib
from email.mime.text import MIMEText

sender_email = "manishwarshalinimanish@gmail.com"

sender_password = "clusabsdcwhhihjx"
receiver_email = "manishwarshalinimanish@gmail.com"

subject = "ShadowLogin Test Mail"

body = "SMTP test successful from Render/Kali"

msg = MIMEText(body)

msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:

    print("Connecting...")

    server = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        timeout=10
    )

    print("Logging in...")

    server.login(
        sender_email,
        sender_password
    )

    print("Sending mail...")

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()

    print("EMAIL SENT SUCCESSFULLY")

except Exception as e:

    print("ERROR:", e)
