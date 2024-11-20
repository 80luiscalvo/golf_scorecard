from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from theme import Theme
from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen
from screens.score_screen import ScoreScreen
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import threading

class ReloadHandler(FileSystemEventHandler):
    """Handles file change events with filters to avoid infinite loops."""
    def __init__(self, app):
        self.app = app

    def on_modified(self, event):
        # Only monitor changes in specific file types
        if event.src_path.endswith((".kv", ".py")):
            # Ignore changes in system-generated or temporary files
            if "__pycache__" in event.src_path or event.src_path.endswith(".pyc"):
                return

            print(f"File changed: {event.src_path}. Restarting the app...")
            os._exit(0)  # Exit the app for a restart

class GolfScorecardApp(App):
    def build(self):
        self.theme = Theme  # Make the theme globally available
        sm = ScreenManager()

        # Add screens
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ScoreScreen(name='score_screen'))

        # Enable hot reload
        self.enable_hot_reload()

        return sm

    def enable_hot_reload(self):
        """Enable file watching and hot reload."""
        event_handler = ReloadHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path=".", recursive=True)

        # Run the observer in a separate thread
        observer_thread = threading.Thread(target=observer.start, daemon=True)
        observer_thread.start()
        print("Hot reload is active. Watching for changes...")

if __name__ == "__main__":
    GolfScorecardApp().run()
