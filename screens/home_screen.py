import json
from pathlib import Path
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):

    def on_enter(self, *args):
        """Reset the current_user.json file with empty data."""
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
