class Time():
    @staticmethod
    def _counter(m, n):
        lis = []
        minute_addin = m // 60
        minute_remains = m % 60
        second_addin = n // 60
        second_remains = n % 60
        if minute_remains < 0:
            minute_remains += 60
            minute_addin -= 1
        if second_remains < 0:
            second_remains += 60
            second_addin -= 1
        lis.append(minute_addin // 60)#Minutes addin
        lis.append(minute_remains % 60)#Minutes remains
        lis.append(second_addin // 60)#Seconds addin
        lis.append(second_remains % 60)#Seconds remains
        return lis
    
    def __init__(self, hours, minutes, seconds):
        if not (isinstance(hours, int) and isinstance(minutes, int)\
                and isinstance(seconds, int)):
            raise TypeError
        lis = Time._counter(minutes, seconds)
        self._hour = hours + lis[0]
        self._minute = lis[1] + lis[2]
        self._second = lis[3]

    def hours(self):
        return self._hour

    def minutes(self):
        return self._minute

    def seconds(self):
        return self._second

    def __add__(self, another):
        hours = self._hour + another.hours()
        minutes = self._minute + another.minutes()
        seconds = self._second + another.seconds()
        return Time(hours, minutes, seconds)

    def __sub__(self, another):
        hours = self._hour - another.hours()
        minutes = self._minute - another.minutes()
        seconds = self._second - another.seconds()
        return Time(hours, minutes, seconds)

    def __lt__(self, another):
        if self._hour != another.hours():
            return self._hour < another.hours()
        elif self._minute != another.minutes():
            return self._minute < another.minutes()
        else:
            return self._second < another.seconds()

    def __eq__(self, another):
        if self._hour == another.hours() and self._minute == \
           another.minutes() and self._second == another.seconds():
            return True
        else:
            return False

    def detail(self):
        print(str(self._hour) + ':' + str(self._minute) + ':' + str(self._second))

#test code
a = Time(23, -8, -6)
b = Time(23, 2, 2)
a.detail()
c = a + b
c.detail()
