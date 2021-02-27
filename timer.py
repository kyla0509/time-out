# import modules
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

        self.tOut = config.getint('settings', 'messageTime')
        self.sleeptime = config.getint('settings', 'sleepTime')
        self.language = config.get('settings', 'language')
        self.runtime = config.getint('settings', 'repeat')

    def run(self):
        i = 0
        while i < self.runtime:
            notification.notify(
                title = "ALERT!!!",
                message = "Take a break! It has been an hour!",
                timeout = self.tOut
            )
            i += 1
            time.sleep(self.sleeptime)

if __name__ == "__main__":
    timeout = TimeOut()

    timeout.run()
