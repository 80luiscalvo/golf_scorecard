from kivy.app import App  # Make sure this import is here
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen
from screens.score_screen import ScoreScreen  # Import ScoreScreen

class GolfScorecardApp(App):
    def build(self):
        sm = ScreenManager()

        # Add screens to ScreenManager
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ScoreScreen(name='score_screen'))  # Add the ScoreScreen

        return sm

if __name__ == '__main__':
    GolfScorecardApp().run()
