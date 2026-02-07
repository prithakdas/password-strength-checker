# Password_checker_Project

## Project Overview
The Password Checker Project is a Flask-based web application that evaluates password
strength and provides security feedback.

This documentation explains how to set up and run the project on Windows and Linux
(Kali/Ubuntu/Debian).

---

## Objectives
- To analyze password strength using security rules
- To promote secure password practices
- To provide a simple and interactive web-based interface

---

## Prerequisites (Both OS)
- Git installed
- Python 3.x installed
- Internet connection

---

## Step-by-Step Installation Guide

### 1. Clone the Repository

#### Windows / Linux
```bash
git clone https://github.com/prithakdas/password-strength-checker.git
cd password-strength-checker
```

---

### 2. Create a Virtual Environment

#### Windows
```powershell
python -m venv venv
```

#### Linux
```bash
python3 -m venv venv
```

---

### 3. Activate Virtual Environment

#### Windows
```powershell
venv\Scripts\activate
```

#### Linux
```bash
source venv/bin/activate
```

After activation, `(venv)` will appear in the terminal.

---

### 4. Install Required Dependencies

#### Windows
```powershell
pip install -r requirements.txt
```

#### Linux
```bash
pip install flask requests
```

If `pip install -r requirements.txt` command fails in Windows, then use:
```powershell
python.exe -m pip install --upgrade pip
```

---

### 5. Run the Application

#### Windows / Linux
```bash
python app.py
```

---

## Access the Application
Open your browser and visit:
```
http://127.0.0.1:5000
```

---

## Project Structure
```text
password-strength-checker/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
```

---

## Notes
- The application runs locally.
- Passwords are not stored.
- Works on Windows, Kali Linux, Ubuntu, Debian.
- Only Python & Flask are required.

---

## Conclusion
This documentation demonstrates how the same Flask project can be executed on both
Windows and Linux, with only minor command differences related to Python and virtual
environment activation.



