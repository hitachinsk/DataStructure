class Assoc():
    def __init__(self, index_,  value_):
        self.key = index_
        self.value = value_

    def __lt__(self, another):
        return self.key < another.key

    def __le__(self, another):
        return self.key <= another.key

    def __str__(self):
        return 'Assoc key is {0}, value is {1}'.format(self.key, self.value)
