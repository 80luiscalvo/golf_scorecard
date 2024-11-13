from kivy.app import App
from kivy.lang import Builder  # Add this import
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ListProperty

# Explicitly load the .kv file
Builder.load_file("golfscorecard.kv")

class GolfScorecard(BoxLayout):
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
        return GolfScorecard()


if __name__ == '__main__':
    GolfScorecardApp().run()
