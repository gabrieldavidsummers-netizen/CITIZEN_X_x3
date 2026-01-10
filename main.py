import os
from kivy.app import App
from kivy.uix.browser import WebView # Note: Requires jnius/android dependencies for APK
from kivy.core.window import Window

# For Kivy-based Android deployment, we serve the local Soul (index.html)
# This bridge ensures the UI persists through the Buildozer anvil.

class SovereignApp(App):
    def build(self):
        # In a real Kivy/Buildozer setup, you would use a WebView widget 
        # to load the index.html generated below.
        pass

if __name__ == '__main__':
    SovereignApp().run()
