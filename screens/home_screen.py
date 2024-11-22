import json
from pathlib import Path
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        """Build the UI components for the HomeScreen."""
        # Main vertical layout
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=[dp(20)] * 4)

        # Welcome Label
        welcome_label = Label(
            text="Welcome to GolfScorecardApp",
            font_size='22sp',
            size_hint=(1, None),
            height=dp(50),
            halign='center',
            valign='middle',
            color=(0.1, 0.1, 0.1, 1)  # Dark gray for text
        )
        welcome_label.bind(size=welcome_label.setter('text_size'))  # Responsive text wrapping
        layout.add_widget(welcome_label)

        # Start Round Button
        start_round_button = Button(
            text="Start the Round",
            size_hint=(1, None),
            height=dp(50),
            background_color=(0.2, 0.6, 0.86, 1),  # Modern blue shade
            color=(1, 1, 1, 1),  # White text
            font_size='18sp',
            on_press=self.go_to_settings_screen
        )
        layout.add_widget(start_round_button)

        # Reset Data Button
        reset_button = Button(
            text="Reset User Data",
            size_hint=(1, None),
            height=dp(50),
            background_color=(0.86, 0.2, 0.2, 1),  # Red for destructive action
            color=(1, 1, 1, 1),  # White text
            font_size='18sp',
            on_press=lambda instance: self.reset_user_data()
        )
        layout.add_widget(reset_button)

        # Add layout to the screen
        self.add_widget(layout)

    def go_to_settings_screen(self, instance):
        """Navigate to the Settings screen."""
        self.manager.current = 'settings'

    def on_enter(self, *args):
        """Called when entering the screen."""
        pass  # Add any dynamic data updates or actions here

    def reset_user_data(self):
        """Writes an empty structure to current_user.json."""
        data_path = Path("data/current_user.json")
        data_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

        empty_data = {
            "current user": [{
                "email": "",
                "PIN_Number": "",
                "handicap": "",
                "course": ""
            }]
        }

        try:
            data_path.write_text(json.dumps(empty_data, indent=4))
            print("User data reset to empty structure.")
        except Exception as e:
            print(f"Error resetting user data: {e}")
