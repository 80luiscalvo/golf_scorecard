import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty

# Sample course data
course_data = {
    "golf_courses": [
        {"name": "Sunnyvale Golf Course"},
        {"name": "Green Valley Country Club"}
    ]
}

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    handicap = NumericProperty(0)
    selected_course = StringProperty("")
    email = StringProperty("")
    pin_number = StringProperty("")
    course_names = ListProperty()

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        # Initialize course_names with the names from course_data
        self.course_names = [course["name"] for course in course_data["golf_courses"]]

    def save_user_data(self):
        # Load existing user data from current_users.json
        try:
            with open("current_users.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {"current user": [{"email": "", "PIN_Number": "", "handicap": "", "course": ""}]}
        
        # Update the current user data
        data["current user"][0]["email"] = self.email
        data["current user"][0]["PIN_Number"] = self.pin_number
        data["current user"][0]["handicap"] = self.handicap
        data["current user"][0]["course"] = self.selected_course

        # Save the updated data back to current_users.json
        try:
            with open("current_users.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            print("User data saved to current_users.json")
        except Exception as e:
            print(f"Error saving data: {e}")

class ScoreScreen(Screen):
    player_name = StringProperty("Player")
    hole_scores = ListProperty([0] * 18)
    total_score = NumericProperty(0)

    def update_score(self, hole, score):
        # Update score for a specific hole
        self.hole_scores[hole - 1] = score
        # Calculate the total score
        self.total_score = sum(self.hole_scores)

class GolfScorecardApp(App):
    def build(self):
        Builder.load_file("golfscorecard.kv")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(ScoreScreen(name="score"))
        return sm

if __name__ == "__main__":
    GolfScorecardApp().run()
