# AI Learning Calendar

This project generates a 90-day AI learning plan as an `.ics` calendar file that you can import into Apple Calendar, Google Calendar, or any app that supports iCalendar.  
Each weekday (Mon–Fri), the system creates a one-hour AI learning event — covering Python, data science, Kaggle, machine learning, fast.ai, Hugging Face, Streamlit, GitHub, and portfolio development.

---

## 🌟 Features

- 90 days of structured AI learning  
- Weekday-only events (auto-skips weekends)  
- Configurable start date  
- Configurable event time (default: **9:00 AM, America/Los_Angeles**)  
- One-click generation using `run.sh`  
- Outputs a clean `.ics` calendar file (~25 KB)

---

## 📦 Requirements

- macOS  
- Python 3  
- Python package: `ics`

Install dependencies:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install ics
---
