from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager
from theme import Theme
from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen
from screens.score_screen import ScoreScreen
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from kivy.clock import Clock
import importlib
import threading


class ReloadHandler(FileSystemEventHandler):
    """Handles file change events for hot reload."""

    def __init__(self, app):
        self.app = app

    def on_modified(self, event):
        if event.src_path.endswith((".kv", ".py")):
            if "__pycache__" in event.src_path or event.src_path.endswith(".pyc"):
                return

            print(f"File changed: {event.src_path}. Reloading the app...")
            self.reload_app()

    def reload_app(self):
        try:
            importlib.reload(screens.home_screen)
            importlib.reload(screens.settings_screen)
            importlib.reload(screens.score_screen)
            importlib.reload(theme)

            # Clear and rebuild widgets in all screens
            for screen in self.app.root.screens:
                screen.clear_widgets()
                screen.build_ui()

        except Exception as e:
            print(f"Error reloading modules: {e}")

        Clock.schedule_once(self.restart_app, 0)

    def restart_app(self, dt):
        self.app.stop()
        self.app.run()


class GolfScorecardApp(App):
    background_color = ListProperty([1, 1, 1, 1])  # Default color

    def build(self):
        self.theme = Theme()
        self.background_color = self.theme.BACKGROUND_COLOR
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ScoreScreen(name='score_screen'))

        self.enable_hot_reload()
        return sm

    def enable_hot_reload(self):
        event_handler = ReloadHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path=".", recursive=True)

        observer_thread = threading.Thread(target=observer.start, daemon=True)
        observer_thread.start()
        print("Hot reload is active. Watching for changes...")


if __name__ == "__main__":
    GolfScorecardApp().run()
