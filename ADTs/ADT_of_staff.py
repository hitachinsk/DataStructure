import ADT_of_person as AP
import datetime as dm

#ADT Staff()
#   Staff(self, str name, str sex, tuple birthday, tuple entey_date, int salary, str position)
#   name(self)
#   sex(self)
#   en_year(self)
#   salary(self)
#   set_salary(self, new_salary)
#   position(self)
#   set_position(self, new_position)
#   birthday(self)
#   detail(self)

class Staff(AP.Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = dm.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)
    
    def __init__(self, name, sex, birthday, entry_date, salary, position):
        if not isinstance(name, str) or sex not in ('male', 'female') or\
           not isinstance(salary, int):
            raise AP.PersonValueError()
        try:
            birth = dm.date(*birthday)
            entry = dm.date(*enter_date)
        except:
            raise AP.PersonValueError()
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._entry_date = entry
        self._position = position
        self._salary = salary

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def en_year(self):
        return self._entry_date.year

    def set_salary(self, new_salary):
        if not isinstance(new_salary, int):
            raise TypeError
        self._salaey = new_salary

    def position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def birthday(self):
        return self._birthday

    def detail(self):
        return ','.join((super.detail(),
                         'entry_date' + str(self._entry_date),
                         'position' + str(self._position),
                         'salary' + str(self._salary)))
