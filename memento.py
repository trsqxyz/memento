#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import sys

class Mori(object):
    """docstring for Mori"""
    def __init__(self, mode=None, times=4):
        self.mode = {
            'mori': self.mori,
            'pomodoro': self.pomodoro,
            None: self.mori
            }
        self.msg = self.life(times)
        self.mode[mode]()

    def time_keeper(self):
        while True:
            try:
                print(next(self.msg))
            except (KeyboardInterrupt, StopIteration) as e:
                raise e
            time.sleep(60*5)

    def mori(self):
        time.sleep(60*5)
        print(next(self.msg))
        try:
            self.time_keeper()
        except (KeyboardInterrupt, StopIteration):
            return

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

    def life(self, times=3, first='*', last=None):
        yield first
        for _ in range(times):
            yield '*'
        if last is None:
            raise StopIteration
        yield last

if __name__ == '__main__':
    m = Mori('mori')
