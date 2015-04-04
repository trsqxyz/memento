#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

class Mori(object):
    """docstring for Mori"""
    def __init__(self, mode=None, sec=60*5):
        self.mode = {
            'mori': self.mori,
            None: self.mori
            }
        self.stop_event = threading.Event()
        self.t = threading.Timer(1, self.mode[mode], (sec,))
        self.t.start()

    def mori(self, sec):
        start_time = time.time()
        while not self.stop_event.is_set():
            print("Mement mori.")
            if sec < time.time() - start_time:
                self.stop()
            time.sleep(sec)

    def stop(self):
        self.stop_event.set()

if __name__ == '__main__':
    m = Mori('mori')
