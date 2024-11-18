from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty, NumericProperty

class ScoreScreen(Screen):
    player_name = StringProperty("Player")
    hole_scores = ListProperty([0] * 18)  # Scores for each hole (18 holes)
    total_score = NumericProperty(0)  # Total score across all holes
    course_data = ListProperty([{'distance': 0, 'par': 0, 'handicap': 0}] * 18)  # List of dicts containing distance, par, and handicap for each hole
    course_name = StringProperty("Course Name")

    def update_score(self, hole_number, score):
        """Update the score for a given hole and recalculate the total score."""
        self.hole_scores[hole_number - 1] = score
        self.total_score = sum(self.hole_scores)

    def set_course_data(self, course_data):
        """Set course data (distance, par, and handicap for each hole)."""
        self.course_data = course_data

    def set_course(self, course):
        """Set the course data for a specific course."""
        self.course_name = course['course_name']
        course_data = []
        
        # Adjust course data to match the hole data structure
        for hole in course['holes']:
            course_data.append({
                'distance': hole['distance']['white'],  # Can choose 'white', 'yellow', etc.
                'par': hole['par'],
                'handicap': hole['handicap']
            })
        
        self.set_course_data(course_data)

    def get_total_score(self):
        """Calculate the total score for all holes."""
        return sum(self.hole_scores)
    
    def get_hole_data(self):
        """Return hole data for RecycleView."""
        return [
            {
                'hole_number': i + 1,  # Hole number 1 through 18
                'score': self.hole_scores[i]  # Current score for the hole
            } for i in range(18)
        ]
