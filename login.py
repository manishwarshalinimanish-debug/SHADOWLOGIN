ip = request.headers.get('X-Forwarded-For', request.remote_addr)

location = get_location(ip)

print("IP:", ip)
print("Country:", location["country"])
print("Region:", location["region"])
print("City:", location["city"])
