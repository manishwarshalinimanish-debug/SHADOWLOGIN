import requests
import threading
from alerts import send_email_alert

attack_logs = []

attempt_counter = {}

BLOCK_LIMIT = 5


def get_location(ip):

    try:

        response = requests.get(
            f"https://ipapi.co/{ip}/json/",
            timeout=5
        )

        data = response.json()

        country = data.get("country_name", "Unknown")

        region = data.get("region", "Unknown")

        return country, region

    except Exception as e:

        print("Location Error:", e)

        return "Unknown", "Unknown"


def send_email_background(log):

    try:

        send_email_alert(log)

    except Exception as e:

        print("Email Error:", e)


def detect_attack(ip, username, password):

    if ip in attempt_counter:
        attempt_counter[ip] += 1
    else:
        attempt_counter[ip] = 1

    attempts = attempt_counter[ip]

    country, region = get_location(ip)

    log = {
        "ip": ip,
        "username": username,
        "password": password,
        "attempts": attempts,
        "country": country,
        "region": region
    }

    attack_logs.append(log)

    print("\n========== ATTACK DETECTED ==========")

    print(log)

    # SAVE LOG
    try:

        with open("attack_logs.txt", "a") as file:

            file.write(
                f"""
IP: {ip}
Username: {username}
Password: {password}
Attempts: {attempts}
Country: {country}
Region: {region}
-------------------------
"""
            )

    except Exception as e:

        print("File Error:", e)

    # SEND EMAIL IN BACKGROUND
    thread = threading.Thread(
        target=send_email_background,
        args=(log,)
    )

    thread.start()

    # BLOCK IP
    if attempts >= BLOCK_LIMIT:

        try:

            with open("blocked_ips.txt", "a") as f:

                f.write(ip + "\n")

            print(f"{ip} BLOCKED")

        except Exception as e:

            print("Block Error:", e)
