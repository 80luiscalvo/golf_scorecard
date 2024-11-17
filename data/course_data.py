import json
from pathlib import Path

def load_course_data():
    data_path = Path("data/course_data.json")
    try:
        data = json.loads(data_path.read_text())
        # Extract course names from the JSON structure
        return [course["name"] for course in data.get("golf_courses", [])]
    except FileNotFoundError:
        print("Course data file not found.")
        return []
    except Exception as e:
        print(f"Error loading course data: {e}")
        return []
