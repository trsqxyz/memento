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
        try:
            time.sleep(60*5)
            self.time_keeper()
        except (KeyboardInterrupt, StopIteration):
            return

    def pomodoro(self):
        done_pomodoro = 0
        short_break = "Done! Take a short break."
        long_break = "Goal! Take a long break."
        begin_pomodoro = "Begin the task."
        perfect_day = "It's a perfect."

        one_pomodoro = (begin_pomodoro, short_break)
        fourth_pomodoro = (begin_pomodoro, None)
        one_long_break = (long_break, None)
        finish = (begin_pomodoro, perfect_day)

        one_goal = tuple(one_pomodoro for _ in range(3)) + \
                    (fourth_pomodoro,) + (one_long_break,)
        last_goal = one_goal[:-1] + (finish,)
        one_day = tuple(one_goal for _ in range(3)) + (last_goal,)

        for goal in one_day:
            for first, last in goal:
                self.msg = self.life(4, first, last)
                try:
                    self.time_keeper()
                except KeyboardInterrupt:
                    print("You've done {0} pomodoro today.".format(done_pomodoro))
                    return
                except StopIteration:
                    if last == short_break:
                        done_pomodoro += 1
                    elif last == perfect_day:
                        print("You've done {0} pomodoro today.".format(done_pomodoro))

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
    m = Mori(mode, times)
