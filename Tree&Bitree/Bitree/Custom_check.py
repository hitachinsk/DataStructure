from random import randint
from link_queue import Linkqueue
from Prior_queue_heap import Prior_queue_heap
from discrete_events_simulation import Simulation
from discrete_events_simulation import Event
#Even if some modles have been imported by prior files, if you want to use them
#in this file, you have to import it again
class Customs_check():
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        #using prior_queue guarantees events can happen in the time sequence
        self.simulation = Simulation(duration)
        self.waitline = Linkqueue()
        self.gate = [0] * gate_num
        self.duration = duration
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval
        self.car_num = 0
        self.total_wait_time = 0
        self.total_used_time = 0

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_acc(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def not_empty_car(self):
        return not self.waitline.is_empty()

    def find_gate(self):
        for i in range(len(self.gate)):
            if self.gate[i] == 0:
                self.gate[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gate[i] == 1:
            self.gate[i] = 0
        else:
            raise ValueError('Free gate error')

    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()

    def statistics(self):
        print('simulate' + str(self.duration) + ' minutes, for ' + str(len(self.gate)) + ' gates.')
        print(str(self.car_num) + ' have passed gates.')
        print('Total wait time is ' + str(self.total_wait_time))
        print('Total used time is ' + str(self.total_used_time))
        print('The average wait time is ' + str(self.total_wait_time / self.car_num))
        print('The average used time is ' + str(self.total_used_time / self.car_num))

class Car():
    def __init__(self, arrive_time):
        self.time = arrive_time

    def arrive_time(self):
        return self.time


def event_log(time, name):
    print('Event ' + str(name) + ' occurs at ' + str(time))

class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'Car Arrive')
        Arrive(time + randint(*customs.arrive_interval), customs)
        car = Car(time)
        if customs.not_empty_car():
            customs.waitline.enqueue(car)
            return
        else:
            i = customs.find_gate()
            if i != None:
                event_log(time, 'Car Check')
                Leave(time + randint(*customs.check_interval), customs, i, car)
            else:
                customs.waitline.enqueue(car)

class Leave(Event):
    def __init__(self, leave_time, customs, gate_num, car):
        Event.__init__(self, leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, 'Car Leave')
        customs.free_gate(self.gate_num)
        customs.car_acc()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.not_empty_car():
            car = customs.waitline.dequeue()
            i = customs.find_gate()
            event_log(time, 'Car Check')
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval), customs, i, car)


if __name__ == '__main__':
    car_arrive_interval = (1, 2)
    car_check_interval = (3, 5)
    cus = Customs_check(3, 480, car_arrive_interval, car_check_interval)
    cus.simulate()
