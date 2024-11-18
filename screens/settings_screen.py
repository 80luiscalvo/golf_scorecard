import json
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Load courses from JSON file
        courses = self.load_courses()

        # Add a label to the settings screen
        label = Label(
            text="Settings Screen",
            font_size="24sp",
            size_hint=(1, 0.2)
        )
        layout.add_widget(label)

        # Add TextInput for Email
        self.email_input = TextInput(
            hint_text="Enter your email",
            size_hint=(1, 0.2),
            multiline=False
        )
        layout.add_widget(self.email_input)

        # Add TextInput for Handicap
        self.handicap_input = TextInput(
            hint_text="Enter your handicap",
            size_hint=(1, 0.2),
            multiline=False
        )
        layout.add_widget(self.handicap_input)

        # Add Spinner for selecting a course
        self.course_spinner = Spinner(
            text='Select Course',
            values=courses,
            size_hint=(1, 0.2),
            height=44
        )
        layout.add_widget(self.course_spinner)

        # Add a button to save the data and start the round
        start_round_button = Button(
            text="Start Round",  # Change the button text to 'Start Round'
            size_hint=(1, 0.2),
            on_press=self.save_settings_and_start_round
        )
        layout.add_widget(start_round_button)

        # Add a button to navigate back to Home Screen
        back_button = Button(
            text="Back to Home",
            size_hint=(1, 0.2),
            on_press=self.go_to_home_screen
        )
        layout.add_widget(back_button)

        self.add_widget(layout)

    def load_courses(self):
        """Load course data from course_data.json"""
        try:
            with open("data/course_data.json", "r") as f:
                data = json.load(f)
                courses = [course["course_name"] for course in data.get("golf_courses", [])]
                return courses
        except Exception as e:
            print(f"Error loading course data: {e}")
            return []

    def save_settings_and_start_round(self, instance):
        """Save settings (email, handicap, course) and navigate to Score Screen"""
        email = self.email_input.text
        handicap = self.handicap_input.text
        course = self.course_spinner.text

        if not email or not handicap or not course:
            # Ensure all fields are filled out before proceeding
            print("Please fill in all fields.")
            return

        # Create the user data dictionary
        user_data = {
            "email": email,
            "handicap": handicap,
            "course": course
        }

        # Path to the current user data file
        current_user_file = "data/current_user.json"

        # Check if the current_user.json file exists
        if os.path.exists(current_user_file):
            # If it exists, load the existing data
            with open(current_user_file, "r") as f:
                current_user = json.load(f)
                # Update the "current user" section with new data
                current_user["current user"][0].update(user_data)
        else:
            # If the file doesn't exist, create an empty structure
            current_user = {
                "current user": [user_data],
                "email": email,
                "handicap": handicap,
                "course": course
            }

        # Save the updated data back to current_user.json
        try:
            with open(current_user_file, "w") as f:
                json.dump(current_user, f, indent=4)
            print("Settings saved successfully.")
        except Exception as e:
            print(f"Error saving user data: {e}")

        # Navigate to the Score screen
        self.manager.current = 'score_screen'  # Ensure 'score_screen' is a valid screen in your ScreenManager

    def go_to_home_screen(self, instance):
        """Navigate back to the Home screen"""
        self.manager.current = 'home'
