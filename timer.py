# import modules
import time
import tkinter as tk
import plyer
from plyer import notification

class TimeOut:
    def __init__(self, runtime):
        self.tOut = 10
        self.sleeptime = 8
        self.language = "mean"
        self.runtime = runtime

    def setLanguage(self, language):
        self.language = language

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
    timeout = TimeOut(5)

    timeout.run()
