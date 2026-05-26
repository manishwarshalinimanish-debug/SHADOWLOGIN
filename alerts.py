import requests
from datetime import datetime


def send_email_alert(log):

    url = "https://api.emailjs.com/api/v1.0/email/send"

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    data = {

        "service_id": "service_farsh1m",

        "template_id": "template_mba73xy",

        "user_id": "OlcuBYOhur4VndMEF",

        "template_params": {

            "ip": log['ip'],

            "username": log['username'],

            "password": log['password'],

            "attempts": log['attempts'],

            "country": log['country'],

            "region": log['region'],

            "time": current_time
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=10
        )

        print(response.text)

        print("EMAILJS ALERT SENT")

    except Exception as e:

        print("EMAILJS ERROR:", e)
