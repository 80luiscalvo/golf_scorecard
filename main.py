from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen
from screens.score_screen import ScoreScreen

class GolfScorecardApp(App):
    def build(self):
        Builder.load_file("golfscorecard.kv")  # Ensure this loads correctly
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))  # Ensure the name matches
        sm.add_widget(ScoreScreen(name="score"))
        return sm

if __name__ == "__main__":
    GolfScorecardApp().run()
