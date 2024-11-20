import json
from pathlib import Path
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = None
        self.build_ui()

    def build_ui(self):
        """Build the UI components for the HomeScreen."""
        if self.layout:  # Prevent duplicate layouts
            return

        # Create the main layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Add a label
        label = Label(
            text="Welcome to the GolfScorecardApp",
            font_size='24sp',
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(label)

        # Add a button to navigate to Settings Screen
        start_round_button = Button(
            text="Start the Round",
            size_hint=(1, 0.2),
            on_press=self.go_to_settings_screen  # Use a method to handle navigation
        )
        self.layout.add_widget(start_round_button)
        
        # Add a button to reset user data
        reset_button = Button(
            text="Reset User Data",
            size_hint=(1, 0.2),
            on_press=lambda instance: self.reset_user_data()
        )
        self.layout.add_widget(reset_button)



        # Add the layout to the screen
        self.add_widget(self.layout)

    def go_to_settings_screen(self, instance):
        """Navigate to the Settings screen."""
        self.manager.current = 'settings'

    def on_enter(self, *args):
        """Called when entering the screen. Resets user data."""
        self.reset_user_data()

    def reset_user_data(self):
        """Writes an empty structure to current_user.json."""
        data_path = Path("data/current_user.json")
        empty_data = {
            "current user": [{
                "email": "",
                "PIN_Number": "",
                "handicap": "",
                "course": ""
            }]
        }

        try:
            # Write the empty data structure to the file
            data_path.write_text(json.dumps(empty_data, indent=4))
            print("User data reset to empty structure.")
        except Exception as e:
            print(f"Error resetting user data: {e}")
