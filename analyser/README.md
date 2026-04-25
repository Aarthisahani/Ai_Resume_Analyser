<div align="center">

# 🧠 AI Resume Analyser

**Stop guessing. Start knowing.**
Upload your resume → Get AI-powered feedback in seconds.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

</div>

---

## ⚡ What is this?

> A full-stack AI web app that analyses your resume like a **hiring manager + ATS system combined**.
> Built with Django + Groq's blazing fast LLaMA 3.1 — results in under 3 seconds.

No fluff. No subscriptions. No data stored on servers. Just raw AI feedback.

---

## 🎯 Features

| Feature | Description |
|---|---|
| 📄 **PDF Upload** | Upload your resume PDF directly |
| 🤖 **AI Analysis** | Powered by Groq LLaMA 3.1 — ultra fast |
| 📊 **ATS Score** | Know if your resume passes ATS filters |
| ✅ **Skills Gap** | See what skills you have vs what's missing |
| 💪 **Strengths** | Know what's working in your resume |
| ⚡ **Improvements** | Exact things to fix — no vague advice |
| 🎯 **Role Suggestions** | AI suggests best-fit job roles for you |
| 🔐 **Auth System** | Login / Signup — your data stays yours |
| 📜 **History** | All your past analyses saved |
| 🖨️ **PDF Report** | Download full analysis as PDF |
| 📧 **Email Report** | Send analysis to any email address |

---

## 🛠️ Tech Stack
Frontend  →  Bootstrap 5.3 + Font Awesome 6
Backend   →  Django 4.2 (Python 3.14)
AI Brain  →  Groq API + LLaMA 3.1 8B Instant
PDF Read  →  pdfplumber
PDF Make  →  ReportLab
Database  →  SQLite (dev) / PostgreSQL (prod)
Auth      →  Django Built-in Auth
Email     →  Gmail SMTP

---

## 🚀 Get Started in 5 Minutes

### 1. Clone
```bash
git clone https://github.com/yourusername/ai-resume-analyser.git
cd ai-resume-analyser
```

### 2. Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install
```bash
pip install -r requirements.txt
```

### 4. Setup `.env`
```bash
SECRET_KEY=django-insecure-your-secret-key
DEBUG=True
GROQ_API_KEY=your_groq_api_key_here
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

> 🔑 Get free Groq API key → [console.groq.com](https://console.groq.com)
> 📧 Gmail App Password → Google Account → Security → App Passwords

### 5. Run
```bash
python manage.py migrate
python manage.py runserver
```

### 6. Open

http://127.0.0.1:8000

---

## 📁 Project Structure
ai-resume-analyser/
│
├── config/                 # Django settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── analyser/               # Main app
│   ├── templates/
│   │   └── analyser/
│   │       ├── index.html      # Upload page
│   │       ├── result.html     # Analysis results
│   │       ├── history.html    # Past analyses
│   │       ├── login.html      # Login page
│   │       ├── signup.html     # Signup page
│   │       └── email_form.html # Email form
│   ├── models.py           # ResumeResult model
│   ├── views.py            # All logic + AI calls
│   └── urls.py             # App routes
│
├── .env                    # Secret keys (never commit!)
├── .gitignore
├── manage.py
└── requirements.txt

---

## 🔮 Roadmap

- [x] PDF Upload & Analysis
- [x] ATS Score
- [x] Login / Signup
- [x] History
- [x] PDF Download
- [x] Email Reports
- [ ] Deploy on Railway
- [ ] AI Resume Builder
- [ ] Compare 2 Resumes
- [ ] Dark Mode
- [ ] Chrome Extension

---

## 🤝 Contributing

Pull requests welcome! Found a bug? Open an issue.

```bash
git checkout -b feature/your-feature
git commit -m "add your feature"
git push origin feature/your-feature
```

---

## 👩‍💻 Author

**Aarthi**
Built with ❤️ and way too much chai ☕

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/yourusername)

---

<div align="center">

**⭐ Star this repo if it helped you land your dream job!**

</div>
Save karo → push karo:
bashgit add .
git commit -m "add modern README"
git push
GitHub pe ekdum fire dikhega! 🔥🚀You said: ek sath do pura me copy pastre karuek sath do pura me copy pastre karu12:32 PMClaude responded: Frontend  →  Bootstrap 5.Deciphered request for complete README file consolidationDeciphered request for complete README file consolidationmarkdown<div align="center">

# 🧠 AI Resume Analyser

**Stop guessing. Start knowing.**
Upload your resume → Get AI-powered feedback in seconds.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

</div>

---

## ⚡ What is this?

> A full-stack AI web app that analyses your resume like a **hiring manager + ATS system combined**.
> Built with Django + Groq's blazing fast LLaMA 3.1 — results in under 3 seconds.

No fluff. No subscriptions. No data stored on servers. Just raw AI feedback.

---

## 🎯 Features

| Feature | Description |
|---|---|
| 📄 **PDF Upload** | Upload your resume PDF directly |
| 🤖 **AI Analysis** | Powered by Groq LLaMA 3.1 — ultra fast |
| 📊 **ATS Score** | Know if your resume passes ATS filters |
| ✅ **Skills Gap** | See what skills you have vs what's missing |
| 💪 **Strengths** | Know what's working in your resume |
| ⚡ **Improvements** | Exact things to fix — no vague advice |
| 🎯 **Role Suggestions** | AI suggests best-fit job roles for you |
| 🔐 **Auth System** | Login / Signup — your data stays yours |
| 📜 **History** | All your past analyses saved |
| 🖨️ **PDF Report** | Download full analysis as PDF |
| 📧 **Email Report** | Send analysis to any email address |

---

## 🛠️ Tech Stack
Frontend  →  Bootstrap 5.3 + Font Awesome 6
Backend   →  Django 4.2 (Python 3.14)
AI Brain  →  Groq API + LLaMA 3.1 8B Instant
PDF Read  →  pdfplumber
PDF Make  →  ReportLab
Database  →  SQLite (dev) / PostgreSQL (prod)
Auth      →  Django Built-in Auth
Email     →  Gmail SMTP

---

## 🚀 Get Started in 5 Minutes

### 1. Clone
```bash
git clone https://github.com/yourusername/ai-resume-analyser.git
cd ai-resume-analyser
```

### 2. Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install
```bash
pip install -r requirements.txt
```

### 4. Setup `.env`
SECRET_KEY=django-insecure-your-secret-key
DEBUG=True
GROQ_API_KEY=your_groq_api_key_here
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password

> 🔑 Get free Groq API key → [console.groq.com](https://console.groq.com)
> 📧 Gmail App Password → Google Account → Security → App Passwords

### 5. Run
```bash
python manage.py migrate
python manage.py runserver
```

### 6. Open
http://127.0.0.1:8000

---

## 📁 Project Structure
ai-resume-analyser/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── analyser/
│   ├── templates/
│   │   └── analyser/
│   │       ├── index.html
│   │       ├── result.html
│   │       ├── history.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── email_form.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── .env
├── .gitignore
├── manage.py
└── requirements.txt

---

## 🔮 Roadmap

- [x] PDF Upload & Analysis
- [x] ATS Score
- [x] Login / Signup
- [x] History
- [x] PDF Download
- [x] Email Reports
- [ ] Deploy on Railway
- [ ] AI Resume Builder
- [ ] Compare 2 Resumes
- [ ] Dark Mode
- [ ] Chrome Extension

---

## 🤝 Contributing

Pull requests welcome! Found a bug? Open an issue.

```bash
git checkout -b feature/your-feature
git commit -m "add your feature"
git push origin feature/your-feature
```

---

## 👩‍💻 Author

**Aarthi**
Built with ❤️ and way too much chai ☕

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/yourusername)

---

<div align="center">

**⭐ Star this repo if it helped you land your dream job!**

</div>
