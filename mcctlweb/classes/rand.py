# rand.py

from threading import Thread, Event
import random
import time
from mcctlweb import socketio

thread = Thread()
thread_stop_event = Event()


class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def random_number_generator(self):
        print("Making random numbers!")
        while not thread_stop_event.is_set():
            number = round(random.random() * 10, 3)
            print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/random-number')
            time.sleep(self.delay)

    def run(self):
        self.random_number_generator()
