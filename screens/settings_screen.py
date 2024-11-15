
# screens/settings_screen.py
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty
import json
import random
from pathlib import Path
from data.course_data import load_course_data

class SettingsScreen(Screen):
    handicap = NumericProperty(0)
    selected_course = StringProperty("")
    email = StringProperty("")
    pin_number = StringProperty("")
    course_names = ListProperty()

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.course_names = load_course_data()
        self.generate_random_pin()

    def generate_random_pin(self):
        self.pin_number = str(random.randint(1000, 9999))

    def save_user_data(self):
        data_path = Path("data/current_user.json")
        try:
            data = json.loads(data_path.read_text())
        except FileNotFoundError:
            data = {"current user": [{"email": "", "PIN_Number": "", "handicap": "", "course": ""}]}
        
        data["current user"][0] = {
            "email": self.email,
            "PIN_Number": self.pin_number,
            "handicap": self.handicap,
            "course": self.selected_course
        }

        try:
            data_path.write_text(json.dumps(data, indent=4))
            print("User data saved to current_user.json")
        except Exception as e:
            print(f"Error saving data: {e}")
