#!/bin/bash
cd "$(dirname "$0")"
rm -f ai_learning_calendar.ics
python3 generate_calendar.py && echo "Updated!" && open ai_learning_calendar.ics
