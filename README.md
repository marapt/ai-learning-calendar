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

### **Change the start date**

Edit:

```python
START_DATE = datetime(2025, 11, 17, tzinfo=TZ)
```

Set any year/month/day — weekends automatically skipped.

Regenerate:

```bash
./run.sh
```

---

### **Edit the task list**

Inside `generate_calendar.py`:

```python
tasks = [
    "[Day 1] Python Ch 1: Intro",
    "[Day 2] Python Ch 2: Variables & Expressions",
    ...
    "[Day 90] FINAL MILESTONE: 2 AI Apps Live + Portfolio"
]
```

You can:

- Replace tasks  
- Add more tasks  
- Remove tasks  

Each task becomes one event.

Regenerate:

```bash
./run.sh
```

---

## 🛠 Updating the Repository

To push your changes to GitHub:

```bash
git status
git add .
git commit -m "Your update description"
git push
```

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `generate_calendar.py` | Main script that builds the 90-day calendar |
| `run.sh` | One-click generator script |
| `ai_learning_calendar.ics` | Generated iCalendar file |
| `README.md` | Project overview & instructions |

---

## 🎉 Happy Learning!

This project helps structure a consistent 90-day learning plan to build strong foundations in Python, ML, and AI tools — all delivered directly to your calendar.
