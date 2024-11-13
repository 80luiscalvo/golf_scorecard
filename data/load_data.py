# data/course_data.py
import json
from pathlib import Path

def load_course_data():
    data_path = Path("data/course_data.json")
    try:
        with data_path.open() as file:
            data = json.load(file)
            return [course["name"] for course in data.get("golf_courses", [])]
    except FileNotFoundError:
        return []
