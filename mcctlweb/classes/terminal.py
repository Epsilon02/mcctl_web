# terminal.py

import time
from random import randrange

from threading import Thread, Event, current_thread
from mcctlweb import socketio

thread = Thread()
thread_stop_event = Event()


class Terminal(Thread):
    def __init__(self):
        self.delay = 3
        super(Terminal, self).__init__()
        self._stop_event = Event()

    def generate_output(self):
        counter = 0
        t = current_thread()
        with open("latest.log") as logfile:
            log = logfile.readlines()
            logfile.close()
        while not self._stop_event.is_set():
            time.sleep(randrange(0, 4))
            if counter < len(log):
                socketio.emit('terminal', log[counter], namespace='/terminal')
                counter = counter + 1

    def run(self):
        self.generate_output()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


class TerminalWrapper():
    def __init__(self):
        self.thread = Thread(target=self.run)

    def run(self):
        terminal = Terminal()
        terminal.start()