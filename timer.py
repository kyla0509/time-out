# import modules
import os
import time
import tkinter as tk
from tkinter import scrolledtext, ttk
import configparser
import plyer
from plyer import notification

class TimeOut:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('timer.ini')
        iconLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        self.tOut = config.getint('settings', 'messageTime')
        self.sleeptime = config.getint('settings', 'sleepTime')
        self.language = config.get('settings', 'language')
        self.runtime = config.getint('settings', 'repeat')
        self.iconPath = os.path.realpath(os.path.join(iconLocation, 'clock.ico'))

    def run(self):
        i = 0
        while i < self.runtime:
            notification.notify(
                title = "ALERT!!!",
                message = "Take a break! It has been an hour!",
                app_icon = self.iconPath,
                timeout = self.tOut
            )
            i += 1
            time.sleep(self.sleeptime)

if __name__ == "__main__":
    timeout = TimeOut()

    timeout.run()
