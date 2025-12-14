# 📬 Bulk Messenger (Email Automation)

A simple yet powerful **Python automation tool** to send a single message to **multiple recipients via email** using SMTP.

Built to practice **real-world OOP**, environment variables, and automation — not toy examples.

---

## 🚀 Features

* Send **bulk emails** with one function call
* Clean **OOP-based design**
* Uses **environment variables** for security
* Gmail SMTP support
* Easy to extend to **WhatsApp / SMS / Slack** later

---

## 🧠 Why this project?

Most beginners learn OOP with fake examples like `Animal` or `Car`.

This project uses:

* a **real problem**
* a **real API (SMTP)**
* a **real workflow**

Exactly how backend systems start in the industry.

---

## 🏗️ Project Structure

```
bulk-msg/
│
├── main.py        # Core BulkMessenger class
├── run.py         # Entry point
├── .env.example   # Environment variable template
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sagarit-code/email-automation.git
cd email-automation
```

### 2️⃣ Install dependencies

```bash
pip install python-dotenv
```

### 3️⃣ Create `.env` file

Create a file named `.env` in the root directory:

```
SENDER_EMAIL=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
```

> ⚠️ Never commit `.env` to GitHub.

---

## ▶️ Usage

```python
from main import BulkMessenger

emails = [
    "user1@example.com",
    "user2@example.com"
]

app = BulkMessenger(
    message="Hey! I won't be coming to play today.",
    emails=emails
)

app.sending()
```

---

## 🔒 Security Notes

* Uses **Gmail App Passwords**
* Secrets are stored using **environment variables**
* `.env` is ignored via `.gitignore`

---

## 🧩 Future Improvements

* Inheritance: `BaseMessenger → EmailMessenger`
* WhatsApp / SMS integration
* CLI support
* Message templates
* Logging & retry logic

---

## 🧑‍💻 Author

Built by **Sagarit**
Learning systems, automation, and backend engineering.

If you found this useful ⭐ star the repo.
