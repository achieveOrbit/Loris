#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" 
Docs for infi.systray -> https://github.com/Infinidat/infi.systray
"""
from infi.systray import SysTrayIcon

import datetime
import time
import sys

#TODO: Add progress for month and year
#TODO: Fullscreen dialog with the passing time (possibly a message window or something)

def date_progress(time_now):
    time_seconds = float((int(time_now.hour)*3600) + (int(time_now.minute)*60) + int(time_now.second))
    percentage_passed_day = "{:.2%}".format(time_seconds/86400.0)
    return percentage_passed_day


def hour_progress(time_now):
    time_seconds = float((int(time_now.minute)*60) + int(time_now.second))
    percentage_passed_hour = "{:.2%}".format(time_seconds/3600.0)
    return percentage_passed_hour


def minute_progress(time_now):
    time_seconds = float(time_now.second)
    percentage_passed_minute = "{:.2%}".format(time_seconds/60)
    return percentage_passed_minute


def on_quit_callback(systray):
    systray.shutdown()
    sys.exit(0)


if __name__ == "__main__":

    menu_options = (("Say Hello", None, date_progress),)
    systray = SysTrayIcon("loris.ico", "Example tray icon", menu_options, on_quit=on_quit_callback)
    systray.start()

    while True:
        time_now = datetime.datetime.now().time()
        percentage_passed_day = "Today's progress: " + str(date_progress(time_now))
        percentage_passed_hour = "Hour's progress: " + str(hour_progress(time_now))
        percentage_passed_minute = "Minute's progress: " + str(minute_progress(time_now))
        hover_text = percentage_passed_day + "\n" + percentage_passed_hour + "\n" + percentage_passed_minute
        systray.update(hover_text = hover_text)
        time.sleep(1)


