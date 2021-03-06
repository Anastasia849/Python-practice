"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Doctor. Новые поля: номер удостоверения, специальность, список текущих
    пациентов (словарь вида номер медицинской книжки: ФИ пациента). Определить конструктор, с вызовом родительского
    конструктора. Определить функции добавления нового пациента, удаления выписанного, форматированной печати
    всех пациентов. Переопределить метод преобразования в строку для печати основной информации (ФИ, возраст,
    номер удостоверения, специальность).
Создать производный от Person класс Nurse. Новые поля: номер удостоверения, отделение работы, график работы
    (словарь вида день недели: часы работы). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения отделения, добавления, удаления и изменения графика работы. Переопределить
    метод преобразования в строку для печати основной информации (ФИ, возраст, номер удостоверения, отделение).
Создать класс Hospital. Поля: название больницы, адрес, список врачей (список экземпляров класса Doctor),
    список медсестер (список экземпляров класса Nurse). Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о больнице (с использованием переопределения в классах Doctor и Nurse).
    Переопределить методы получения количества врачей функцией len, получения врача по индексу, изменения
    по индексу, удаления по индексу (пусть номера врачей считаются с 1, а индекс 0 – список всех медсестер).
    Переопределить операции + и - для добавления или удаления врача. Добавить функцию создания txt-файла и
    записи всей информации в него (в том числе пациентов врачей и графика работы медсестер).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""

import doctor
import nurse
import hospital
import pickle

file = open("logs.txt", 'w')
file.close()
doctors = []
nurses = []

doctor1 = doctor.Doctor('Александр', 'Иванов', 35, 1, "Хирург")
doctor1.list_update({11112: 'Коннов'})
doctor1.list_update({11113: 'Иванов'})
doctor1.list_update({11114: 'Смирнов'})
doctor2 = doctor.Doctor('Максим', 'Смирнов', 30, 2, 'Терапевт')
doctor2.list_update({11115353: 'Ивашин'})

nurse1 = nurse.Nurse('Анна', 'Иванова', 20, 1, 'Хирургия')
nurses.append(nurse1)
nurse1.update_work_schedule({'понедельник': '9:00-15:00', 'Среда': '15:00-21:00'})
nurse2 = nurse.Nurse('Елена', 'Кудоявцева', 22, 2, 'Гинекология')
nurses.append(nurse2)
nurse2.update_work_schedule({'Вторник': '9:00-15:00', 'Пятница': '9:00-15:00'})

hospital1 = hospital.Hospital('Больница №1', 'Гагарина 7', doctors, nurses)
hospital1 + doctor1
hospital1 + doctor2
hospital1.write_in_file()
doctor3 = doctor.Doctor('Анна', 'Онищенко', 30, 3, 'Гинеколог')
hospital1 + doctor3

with open('doctors_nurses.pickle', 'wb') as f:
    pickle.dump([doctors,nurses], f)


