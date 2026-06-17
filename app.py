from flask import Flask, render_template, request, redirect
from detector import detect_attack, attack_logs

app = Flask(__name__)

REAL_USERNAME = "admin"
REAL_PASSWORD = "admin123"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    ip = request.remote_addr

    if username == REAL_USERNAME and password == REAL_PASSWORD:
        return "<h2>Login Successful</h2>"

    else:
        detect_attack(ip, username, password)
        return "<h3>Wrong Username or Password</h3>"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", logs=attack_logs)

if __name__ == "__main__":
    app.run( port=5000)
