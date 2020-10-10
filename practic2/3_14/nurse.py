import person
import Log


class Nurse(person.Person):

    def __init__(self, name, surname, age, id_number, department):
        person.Person.__init__(self, name, surname, age)
        self._id_number = id_number
        self._department = department
        self._work_schedule = {}
        Log.log('CRE', 'Nurse object is created.')

    def change_department(self, department):
        self._department = department
        Log.log('INF', 'Nurse object change department')

    # изменяет график работы или добавляет новые часы
    def update_work_schedule(self, dict1):
        self._work_schedule.update(dict1)
        Log.log('INF', 'Nurse object change work schedule')

    # удаляет часы работы в определенный день
    def removal_work_schedule(self, key):
        del self._work_schedule[key]
        Log.log('INF', 'Nurse object change work schedule')

    # удаляет все расписание
    def removal_all_work_schedule(self):
        self._work_schedule.clear()
        Log.log('INF', 'Nurse object change work schedule')

    def all_info(self):
        str1 = ''
        for x, y in self._work_schedule.items():
            str1 += '{} : {}\n'.format(x, y)
        return "{} {} {} {} {}\n".format(self._name, self._surname, str(self._age), str(self._id_number),
                                         self._department) + str1

    def __str__(self):
        return "{} {} {} {} {}\n".format(self._name, self._surname, str(self._age), str(self._id_number),
                                         self._department)
