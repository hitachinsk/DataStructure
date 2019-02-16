import ADT_of_person as AP
import datetime as dm
#ADT Student(Person):
#   Student(self, str name, str sex, tuple birthday, str department)
#   department(self)
#   en_year(self)
#   scores(self, course_name)
#   set_course(self, str course_name)
#   set_score(self, str course_name, int score)

class Student(AP.Person):
    _num = 0
    def __init__(self, name, sex, entry_date, department):
        if not isinstance(name, str) or not isinstance(department, str) or \
           sex not in ('male', 'female'):
            raise AP.PersonValueError()
        try:
            ed = dm.date(*entry_date)
        except:
            raise AP.PersonValueError()
        self._name = name
        self._sex = sex
        self._entry_date = ed
        self._department = department
        self._course = {}
        Student._num += 1

    def department(self):
        return self._department
    def en_year(self):
        return self._entry_date.year()
    def set_course(self, course_name):
        self._course[course_name] = None
    def score(self, course_name):
        if course_name not in self._course:
            raise AP.PersonValueError('wrong course name')
        return self._course[course_name]
    def set_score(self, course_name, score):
        if not isinstance(score, int):
            raise AP.PersonValueError()
        self._course[course_name] = score
        
