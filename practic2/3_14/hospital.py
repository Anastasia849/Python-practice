import doctor
import Log


class Hospital:
    def __init__(self, name, address, doctors, nurses):
        self._name = name
        self._address = address
        self._doctors_list = doctors
        self._nurses_list = nurses
        Log.log('CRE', 'Hospital object is created.')

    # переопределение '+','-'
    def __add__(self, doctor1):
        self._doctors_list.append(doctor1)
        Log.log('INF', 'Doctor object is added.')
        return self._doctors_list

    def __sub__(self, doctor1):
        try:
            for i in range(len(self._doctors_list)):
                if self._doctors_list[i] == doctor1:
                    del self._doctors_list[i]
                    Log.log('INF', 'Doctor object is removed.')
                    return self._doctors_list
        except IndexError:
            Log.log('ERR', 'Index error.')
            print('Error')

    def __str__(self):
        str1 = self._name + '\n' + self._address + '\n' + 'Список врачей:\n'
        for i in range(len(self._doctors_list)):
            str1 += self._doctors_list[i].all_info()
        str1 += 'Список медсестёр:\n'
        for i in range(len(self._nurses_list)):
            str1 += self._nurses_list[i].all_info()
        return str1

    def write_in_file(self):
        try:
            file = open('{}.txt'.format(self._name), 'w')
            file.write(self.__str__())
            file.close()
        except  FileNotFoundError:
            print('Файл не создан.\n')

    def __getitem__(self, index):
        if index == 0:
            for i in range(len(self._nurses_list)):
                return self._nurses_list[i].all_info()
        else:
            return self._doctors_list[index - 1]

    def __setitem__(self, index, value):
        if index == 0:
            for i in range(len(self._nurses_list)):
                return self._nurses_list[i].all_info()
        else:
            self._doctors_list[index - 1] = value
            Log.log('INF', 'Doctor object is changed.')

    def __delitem__(self, index):
        if index == 0:
            for i in range(len(self._nurses_list)):
                return self._nurses_list[i].all_info()
        else:
            try:
                del self._doctors_list[index - 1]
                Log.log('INF', 'Doctor object is removed.')
            except IndexError:
                Log.log('ERR', 'Index error.')
                print("Wrong index")

    def __len__(self):
        return len(self._doctors_list)
