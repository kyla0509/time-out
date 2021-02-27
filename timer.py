# import modules
import time
import tkinter
from plyer import notification

class TimeOut:
    def __init__(self, runtime):
        self.tOut = 10
        self.sleeptime = 8
        self.language = "mean"
        self.runtime = runtime

    def setLanguage(self, language):
        self.language = language

    def running(self, runtime, tOut, sleeptime):
        i = 0
        while i < runtime:
            notification.notify(
                title = "ALERT!!!",
                message = "Take a break! It has been an hour!",
                timeout = 
            )
            time.sleep(3600)

if __name__ == "__main__":
    timeout = TimeOut(5)
