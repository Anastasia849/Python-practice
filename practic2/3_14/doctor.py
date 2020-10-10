import person
import hospital
import Log

class Doctor(person.Person):

    def __init__(self, name, surname, age, id_number, speciality):
        person.Person.__init__(self, name, surname, age)
        self._id_number = id_number
        self._speciality = speciality
        self._patients_list = {}
        Log.log('INF', 'Doctor object is created')

    def list_update(self, dict1):
        try:
            self._patients_list.update(dict1)
            Log.log('INF', 'Doctor object change list.')
        except TypeError as err:
            Log.log('Err',err)
            print('Error')

    def list_removal(self, key):
        try:
            del self._patients_list[key]
            Log.log('INF', 'Doctor object change list.')
        except KeyError as err:
            Log.log('Err', err)
            print('Error')

    def print_patients(self):
        print('Список пациентов:')
        print(*self._patients_list.values(), sep='\n')

    def all_info(self):
        str1 = 'Список пациентов:\n'
        for i in self._patients_list.values():
            str1 += i + '\n'
        return "{} {} {} {} {}\n".format(self._name, self._surname, str(self._age), str(self._id_number),
                                         self._speciality) + str1

    def __str__(self):
        return "{} {} {} {} {}\n".format(self._name, self._surname, str(self._age), str(self._id_number),
                                         self._speciality)
