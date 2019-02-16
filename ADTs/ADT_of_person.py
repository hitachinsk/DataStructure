import datetime
#ADT Person:
#   Person(self, str name, str sex, tuple birthday, str ident)  initialize
#   id(self)    get PersonID
#   name(self)  get Person name
#   sex(self)   get Person Sex
#   birthday(self)  get Person Birthday
#   age(self)   get Person age
#   set_name(self, str name)    set Person.name
#   <(self, Person another) compare ID between these two object
#   details(self)   print details of the class

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass


class Person():
    _num = 0
    def __init__(self, name, sex, birthday, ident):
        if not isinstance(name, str) or sex not in ('male', 'female'):
            raise PersonValueError()
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1
    def id(self):
        return self._id
    def name(self):
        return self._name
    def sex(self):
        return self._sex
    def birthday(self):
        return self._birthday
    def age(self):
        return datetime.today.year() - self._birthday.year
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError('set_name', name)
        self._name = name
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another.id()
    def details(self):
        print('The Person' + '\'s id is ' + str(self._id) + '\'s name is ' \
              + self._name + '\'s sex is ' + self._sex + '\'s birthday is '\
              + str(self.birthday))



        
