# 🔐 SHADOWLOGIN

## Secure Authentication & Suspicious Login Detection System

SHADOWLOGIN is a secure authentication and login monitoring system developed using Python and Django. The project is designed to strengthen user account security by tracking login attempts, detecting suspicious activities, recording login metadata, and sending real-time alerts for unauthorized access attempts.

---

## 🚀 Features

* ✅ User Registration and Authentication
* ✅ Secure Password Hashing
* ✅ Login and Logout Management
* ✅ Session-Based Authentication
* ✅ Failed Login Attempt Tracking
* ✅ Suspicious Login Detection
* ✅ IP Address Monitoring
* ✅ Geolocation Tracking (Country, Region, City)
* ✅ Email Alerts for Unauthorized Login Attempts
* ✅ Login Activity Logging
* ✅ User Dashboard
* ✅ Admin Management Panel
* ✅ Responsive User Interface

---

## 🛡️ Security Features

* Password hashing using Django's authentication system
* Protection against unauthorized access
* Session management and secure cookies
* Login attempt monitoring and logging
* CSRF protection
* Form validation and input sanitization
* Email notifications for suspicious activities

---

## 🏗️ System Workflow

1. User enters login credentials.
2. System captures the user's IP address.
3. Geolocation information is retrieved.
4. Credentials are validated against the database.
5. If authentication succeeds:

   * User session is created.
   * Access is granted to the dashboard.
6. If authentication fails:

   * Failed attempt is recorded.
   * Suspicious activity is logged.
   * Email alerts are generated if necessary.

---

## 🛠️ Technology Stack

### Backend

* Python

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* SQLite (Development)
* MySQL (Production Ready)

### APIs & Services

* IP Geolocation API
* SMTP Email Services

### Tools

* Git
* GitHub

---

## 📂 Project Structure

```text
SHADOWLOGIN/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── shadowlogin/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/SHADOWLOGIN.git
cd SHADOWLOGIN
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/

## 📸 Example Suspicious Login Alert

```text
A suspicious login attempt has been detected.

IP Address : 49.xxx.xxx.xxx
Country    : India
Region     : Tamil Nadu
City       : Chennai
Username   : example_user
Attempts   : 3
Time       : 2026-06-17 10:30:25
```

## 🎯 Objectives

* Enhance authentication security.
* Detect unauthorized login attempts.
* Monitor user login activities.
* Provide real-time security notifications.
* Improve account protection mechanisms.


## 🔮 Future Enhancements

* Multi-Factor Authentication (MFA)
* OTP-Based Login Verification
* Face Recognition Authentication
* Fingerprint Authentication
* AI-Based Threat Detection
* Device Fingerprinting
* Real-Time Security Dashboard
* Docker and Cloud Deployment

## 👨‍💻 Author

**Manishwar Manish**
Cybersecurity & Networking Enthusiast
Python | Django | Ethical Hacking | Network Security

## 📜 License

This project is licensed under the MIT License.

⭐ If you found this project useful, please consider giving it a star on GitHub.
