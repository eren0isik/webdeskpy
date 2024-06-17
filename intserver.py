import os
import sys
from threading import Thread
from flask import Flask
import signal

class Greap:
    def __init__(self, title="WebDeskPy", locationx=100, locationy=100, width=800, height=600, folder=None, uiloc="/"):
        self.title = title
        self.locationx = locationx
        self.locationy = locationy
        self.width = width
        self.height = height
        self.folder = folder
        self.uiloc = uiloc
        self.app = Flask(__name__, template_folder=self.folder)

    def run_server(self):
        self.app.run(debug=False, port=6091, use_reloader=False)

    def start(self):
        self.server_thread = Thread(target=self.run_server)
        self.server_thread.start()
        self.run_ui()

    def run_ui(self):
        from ui import UiStart
        UiStart(self.title, self.locationx, self.locationy, self.width, self.height, self.uiloc)
        self.stop()

    def stop(self):
        # Function to gracefully shutdown the Flask server
        os.kill(os.getpid(), signal.SIGINT)
