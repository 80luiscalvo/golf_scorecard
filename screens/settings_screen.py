from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty
import json
import random
from pathlib import Path
from data.course_data import load_course_data  # Import the load_course_data function

class SettingsScreen(Screen):
    handicap = NumericProperty(0)
    selected_course = StringProperty("")
    email = StringProperty("")  # Property to hold email input
    pin_number = StringProperty("")
    course_names = ListProperty()

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        try:
            # Load course names from the JSON file
            self.course_names = load_course_data()
            print("Courses loaded:", self.course_names)
        except Exception as e:
            print(f"Error loading course data: {e}")
            self.course_names = []  # Default to empty if loading fails

        self.generate_random_pin()

    def generate_random_pin(self):
        """Generates a random PIN."""
        self.pin_number = str(random.randint(1000, 9999))

    def update_selected_course(self, course_name):
        """Updates the selected course when a course is picked from the spinner."""
        self.selected_course = course_name
        print(f"Selected course: {self.selected_course}")

    def save_user_data(self):
        """Saves user data to current_user.json."""
        data_path = Path("data/current_user.json")
        try:
            if data_path.exists():
                data = json.loads(data_path.read_text())
            else:
                data = {"current user": [{"email": "", "PIN_Number": "", "handicap": "", "course": ""}]}

            data["current user"][0] = {
                "email": self.email,  # Include email
                "PIN_Number": self.pin_number,
                "handicap": self.handicap,
                "course": self.selected_course
            }

            data_path.write_text(json.dumps(data, indent=4))
            print("User data saved to current_user.json")
        except Exception as e:
            print(f"Error saving data: {e}")
