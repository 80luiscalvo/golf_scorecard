# screens/score_screen.py
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty, NumericProperty

class ScoreScreen(Screen):
    player_name = StringProperty("Player")
    hole_scores = ListProperty([0] * 18)
    total_score = NumericProperty(0)

    def update_score(self, hole, score):
        self.hole_scores[hole - 1] = score
        self.total_score = sum(self.hole_scores)
