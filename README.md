# AI Learning Calendar

This project generates a 90-day AI learning plan as an `.ics` calendar file that you can import into Apple Calendar, Google Calendar, or any calendar app that supports iCalendar.  
Each weekday (Mon–Fri), the system creates a one-hour AI learning task — covering Python, data science, Kaggle, machine learning, fast.ai, Hugging Face, Streamlit, GitHub, and portfolio development.

---

## 🌟 Features

- 90 days of structured AI learning  
- Weekday-only events (auto-skips weekends)  
- Configurable start date  
- Configurable event time (default: **9:00 AM PST**)  
- One-click generation using `run.sh`  
- Outputs a clean `.ics` calendar file (~25 KB)

---

## 🚀 Getting Started

### **1. Clone the repository**

```bash
git clone https://github.com/marapt/ai-learning-calendar.git
cd ai-learning-calendar
```

### **2. Generate the `.ics` calendar**

```bash
./run.sh
```

This will:

- Remove any previous `ai_learning_calendar.ics`  
- Run `generate_calendar.py`  
- Open the new `.ics` file automatically  

Expected output:

```
ai_learning_calendar.ics created! (~25 KB)
Calendar updated!
```

---

## 📥 Importing Into a Calendar

### **Apple Calendar (macOS)**

1. Open Finder → go to the project folder  
2. Double-click `ai_learning_calendar.ics`  
3. Choose a calendar → click **Add**  

### **Google Calendar**

1. Open Google Calendar  
2. Go to **Settings → Import & Export**  
3. Choose the `.ics` file  
4. Select a target calendar  
5. Click **Import**

---

## 🔧 Customization

### **Change the event time**

In `generate_calendar.py`, edit:

```python
EVENT_TIME = time(9, 0)  # 9 AM
```

Examples:

- 7 PM → `time(19, 0)`
- 8:30 AM → `time(8, 30)`

Regenerate:

```bash
./run.sh
```

---
