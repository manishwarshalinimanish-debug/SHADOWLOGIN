import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "manishwarshalinimanish@gmail.com"
EMAIL_PASSWORD = "clus absd cwhh ihjx"

def send_alert(message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = 'ShadowLogin Alert'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.send_message(msg)
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Email Error:", e)
