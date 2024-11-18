from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Add a label to the settings screen
        label = Label(
            text="Settings Screen",
            font_size="24sp",
            size_hint=(1, 0.2)
        )
        layout.add_widget(label)

        # Add a button to navigate back to Home Screen
        back_button = Button(
            text="Back to Home",
            size_hint=(1, 0.2),
            on_press=self.go_to_home_screen
        )
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home'
