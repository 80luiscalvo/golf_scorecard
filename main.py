from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty
import json

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
    course_names = ListProperty()  # Add course_names as a ListProperty

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        # Initialize course_names with the names from course_data
        self.course_names = [course["name"] for course in course_data["golf_courses"]]

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
