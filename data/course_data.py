import json
from pathlib import Path

def load_course_data():
    data_path = Path("data/course_data.json")
    try:
        data = json.loads(data_path.read_text())
        return data.get("courses", [])
    except FileNotFoundError:
        print("Course data file not found.")
        return []
    except Exception as e:
        print(f"Error loading course data: {e}")
        return []
