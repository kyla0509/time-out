# import modules
import os
import time
import tkinter as tk
from tkinter import scrolledtext, ttk
import configparser
import plyer
from plyer import notification
import sys

class TimeOut:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('timer.ini')
        self.iconLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        self.tOut = self.config.getint('settings', 'messageTime')
        self.sleeptime = self.config.getint('settings', 'sleepTime')
        self.language = self.config.get('settings', 'language')
        self.runtime = self.config.getint('settings', 'repeat')
        self.iconPath = os.path.realpath(os.path.join(self.iconLocation, 'clock.ico'))

    def run(self):
        i = 0
        while i < self.runtime:
            alert = setMessage(self, i)
            msgTitle = setTitle(self.language)
            notification.notify(
                title = msgTitle,
                message = alert,
                app_icon = self.iconPath,
                timeout = self.tOut
            )
            i += 1
            time.sleep(self.sleeptime)

def setTitle(lang):
    if lang == "pirate":
        return "ahoy matey,"
    elif lang == "owo":
        return "OwO"
    elif lang =="normal":
        return "hello friend,"
    elif lang =="eldritch":
        return "greetings dreamer,"
    else:
        return "SUP NERD,"

def setMessage(self, i):
        line = i % self.runtime
        if self.language == "pirate":
            langFile = open(os.path.join(os.path.dirname(__file__), 'pirateTalk'))
            message = langFile.readlines()
            return message[line]
        elif self.language == "owo":
            langFile = open(os.path.join(os.path.dirname(__file__), 'owoTalk'))
            message = langFile.readlines()
            return message[line]
        elif self.language == "normal":
            langFile = open(os.path.join(os.path.dirname(__file__), 'normalTalk'))
            message = langFile.readlines()
            return message[line]
        elif self.language == "eldritch":
            langFile = open(os.path.join(os.path.dirname(__file__), 'eldritchTalk'))
            message = langFile.readlines()
            return message[line]
        else:
            langFile = open(os.path.join(os.path.dirname(__file__), 'pirateTalk'))
            message = langFile.readlines()
            return message[line]

if __name__ == "__main__":
    timeout = TimeOut()

    timeout.run()
