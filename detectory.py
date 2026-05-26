attack_logs = []

failed_attempts = {}

blocked_ips = []


def detect_attack(ip, wrong_password):

    global attack_logs
    global failed_attempts
    global blocked_ips

    if ip not in failed_attempts:

        failed_attempts[ip] = 1

    else:

        failed_attempts[ip] += 1

    attempts = failed_attempts[ip]

    log = {

        "ip": ip,

        "country": "India",

        "state": "Tamil Nadu",

        "city": "Chennai",

        "attempts": attempts,

        "password": wrong_password
    }

    attack_logs.append(log)

    print(log)

    if attempts >= 3:

        blocked_ips.append(ip)

        print("[SOC ALERT] Brute Force Attack")

        return True

    return False
