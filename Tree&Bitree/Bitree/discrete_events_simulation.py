from random import randint
from link_queue import Linkqueue
from Prior_queue_heap import Prior_queue_heap

class Simulation():
    def __init__(self, duration):
        #using prior_queue guarantees events can happen in the time sequence
        self._eventq = Prior_queue_heap()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Event():
    def __init__(self, time, host):
        self._ctime = time
        self._host = host

    def __lt__(self, another):
        return self._ctime < another._ctime

    def __le__(self, another):
        return self._ctime <= another._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):
        pass
