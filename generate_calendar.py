#!/usr/bin/env python3
from ics import Calendar, Event
from ics.grammar.parse import ContentLine
from datetime import datetime, timedelta, time
import zoneinfo

TZ = zoneinfo.ZoneInfo("America/Los_Angeles")
START_DATE = datetime(2025, 11, 17, tzinfo=TZ)  # Mon, Nov 17
EVENT_TIME = time(9, 0)  # 9 AM

tasks = [
    "[Day 1] Python Ch 1: Intro",
    "[Day 2] Python Ch 2: Variables & Expressions",
    "[Day 3] Python Ch 3: Conditional Code",
    "[Day 4] Python Ch 4: Functions",
    "[Day 5] Python Ch 5: Loops & Iteration",
    "[Day 6] Python Ch 6: Strings",
    "[Day 7] Mini-Project: Build Calculator in Colab",
    "[Day 8] Kaggle Python Lesson 1: Hello Python",
    "[Day 9] Kaggle Lesson 2: Functions & Syntax",
    "[Day 10] Kaggle Lesson 3: Booleans & Conditionals",
    "[Day 11] Kaggle Lesson 4: Lists",
    "[Day 12] Kaggle Lesson 5: Loops & Comprehensions",
    "[Day 13] Kaggle Lesson 6: Strings & Dicts",
    "[Day 14] Finish Kaggle Python + Earn Badge",
    "[Day 15] Khan: Vectors Intro",
    "[Day 16] Khan: Vector Operations",
    "[Day 17] 3B1B: Derivative Intro",
    "[Day 18] Khan: Matrices Intro",
    "[Day 19] Khan: Matrix Multiplication",
    "[Day 20] 3B1B: Chain Rule",
    "[Day 21] Explain Gradient in 1 Min (Voice Note)",
    "[Day 22] Install Anaconda + VS Code",
    "[Day 23] NumPy Quickstart: Arrays",
    "[Day 24] NumPy: Indexing & Broadcasting",
    "[Day 25] Pandas 10-min Guide",
    "[Day 26] Pandas: Filtering & Grouping",
    "[Day 27] Load Titanic CSV to df.head()",
    "[Day 28] MILESTONE: Share Colab df.describe()",
    "[Day 29] Andrew Ng Week 1: Intro",
    "[Day 30] Andrew Ng: Linear Regression",
    "[Day 31] Andrew Ng: Cost Function",
    "[Day 32] Andrew Ng: Gradient Descent",
    "[Day 33] Andrew Ng: Multivariate Linear Reg",
    "[Day 34] Andrew Ng: Computing Parameters",
    "[Day 35] Andrew Ng: Normal Equation",
    "[Day 36] Finish Kaggle Intro to ML",
    "[Day 37] Kaggle Intermediate ML: Lesson 1",
    "[Day 38] Kaggle Intermediate ML: Lesson 2",
    "[Day 39] Kaggle Intermediate ML: Lesson 3",
    "[Day 40] Kaggle Intermediate ML: Lesson 4",
    "[Day 41] Kaggle Intermediate ML: Lesson 5",
    "[Day 42] Kaggle Intermediate ML: Lesson 6",
    "[Day 43] Fork Titanic Competition",
    "[Day 44] EDA: nulls + plots",
    "[Day 45] Train Logistic Regression to Submit",
    "[Day 46] Try Random Forest",
    "[Day 47] Try XGBoost",
    "[Day 48] Submit Best Model (>0.78)",
    "[Day 49] Kaggle: Cross-Validation",
    "[Day 50] Kaggle: Pipelines",
    "[Day 51] Kaggle: Feature Engineering",
    "[Day 52] Kaggle: Model Tuning",
    "[Day 53] Kaggle: Final Submission",
    "[Day 54] fast.ai: Lesson 1 Setup",
    "[Day 55] fast.ai: Lesson 1 - First Model",
    "[Day 56] fast.ai: Lesson 2 - Data Block",
    "[Day 57] fast.ai: Lesson 3 - Training",
    "[Day 58] fast.ai: Lesson 4 - Deploy",
    "[Day 59] Build Pet Classifier",
    "[Day 60] Export Model (.pkl)",
    "[Day 61] Hugging Face: Ch 1 - Intro",
    "[Day 62] Hugging Face: Ch 2 - Tokenizers",
    "[Day 63] Hugging Face: Ch 3 - Models",
    "[Day 64] Hugging Face: Ch 4 - Fine-tuning",
    "[Day 65] Hugging Face: Ch 5 - Pipelines",
    "[Day 66] Build Text Classifier",
    "[Day 67] Streamlit: Setup & Hello World",
    "[Day 68] Streamlit: Image Upload",
    "[Day 69] Streamlit: Connect Model",
    "[Day 70] Deploy Image App",
    "[Day 71] Streamlit: Text Input",
    "[Day 72] Connect HF Model",
    "[Day 73] Deploy Text App",
    "[Day 74] GitHub: Create Repo",
    "[Day 75] GitHub: Add README",
    "[Day 76] GitHub: Push Code",
    "[Day 77] GitHub: Add Screenshots",
    "[Day 78] Finalize Portfolio",
    "[Day 79] Share on LinkedIn",
    "[Day 80] Share on X/Twitter",
    "[Day 81] Review All Code",
    "[Day 82] Fix Bugs",
    "[Day 83] Write Blog Post",
    "[Day 84] Publish Blog",
    "[Day 85] Record Demo Video",
    "[Day 86] Upload to YouTube",
    "[Day 87] Update Resume",
    "[Day 88] Apply to 3 AI Roles",
    "[Day 89] Celebrate!",
    "[Day 90] FINAL MILESTONE: 2 AI Apps Live + Portfolio"
]

cal = Calendar()
cal.extra.append(ContentLine(name="X-WR-TIMEZONE", value="America/Los_Angeles"))

current = START_DATE
for task in tasks:
    while current.weekday() >= 5:
        current += timedelta(days=1)
    ev = Event()
    ev.name = task
    ev.begin = datetime.combine(current.date(), EVENT_TIME, tzinfo=TZ)
    ev.end = ev.begin + timedelta(hours=1)
    ev.description = "90-Day AI Plan\nhttps://github.com/marapt/ai-learning-calendar"
    ev.alarms = [{"action": "DISPLAY", "description": "Time to learn!", "trigger": "-PT1M"}]
    cal.events.add(ev)
    current += timedelta(days=1)

with open("ai_learning_calendar.ics", "w", encoding="utf-8", newline='\n') as f:
    f.writelines(cal.serialize_iter())

print("Calendar created! (~25 KB)")
