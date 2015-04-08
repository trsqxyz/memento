#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import sys

class Mori(object):
    """docstring for Mori"""
    def __init__(self, mode=None, times=5):
        self.mode = {
            'mori': self.mori,
            'pomodoro': self.pomodoro,
            None: self.mori
            }
        self.msg = self.life(times)
        self.stop_event = threading.Event()
        self.t = threading.Timer(1, self.mode[mode])
        self.t.start()

    def mori(self):
        while not self.stop_event.is_set():
            try:
                print(next(self.msg))
                time.sleep(60*5)
            except (KeyboardInterrupt, StopIteration):
                self.stop()

    def pomodoro(self):
        short_break = "Done! Take a short break."
        long_break = "Goal! Take a long break."
        begin_pomodoro = "Begin to the task."
        perfect_day = "You've done {0} tasks today. It's a perfect.".format(done_tasks)
        one_pomodoro = [short_break, begin_pomodoro]
        one_goal = [long_break] + one_pomodoro * 4
        one_day = one_goal * 4

        while not self.stop_event.is_set():
            try:
                print(next(self.msg))
                time.sleep(60*5)
            except (KeyboardInterrupt, StopIteration):
                self.stop()

    def stop(self):
        self.stop_event.set()

    def life(self, times, m=None):
        for _ in range(times):
            if m is None: m = '*'
            m = yield m

if __name__ == '__main__':
    m = Mori('mori')
