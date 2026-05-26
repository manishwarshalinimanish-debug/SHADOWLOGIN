import requests
from alerts import sound_alert, send_email_alert

attack_logs = []

attempt_counter = {}

BLOCK_LIMIT = 5

def get_location(ip):

    try:
        data = requests.get(f"https://ipapi.co/{ip}/json/").json()

        country = data.get("country_name", "Unknown")
        region = data.get("region", "Unknown")

        return country, region

    except:
        return "Unknown", "Unknown"

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

    sound_alert()

    send_email_alert(log)

    if attempts >= BLOCK_LIMIT:

        with open("blocked_ips.txt", "a") as f:
            f.write(ip + "\n")

        print(f"{ip} BLOCKED")
