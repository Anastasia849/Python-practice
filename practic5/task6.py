import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from bs4 import BeautifulSoup
import re
import requests
import json
import xlrd
import datetime


def get_schedule_from_mirea():
    page = requests.get('https://www.mirea.ru/schedule/')
    soup = BeautifulSoup(page.text, "html.parser")

    result = soup.find('div', {'class': 'rasspisanie'}).find(string='Институт информационных технологий').find_parent(
        'div').find_parent('div').findAll('a', {'class': 'uk-link-toggle'})
    for x in result:
        if re.search('ИИТ.*xlsx', str(x)):
            if re.search('1к', str(x)):
                f = open('file1.xlsx', 'wb')
                filexlsx = requests.get(x['href'])
                f.write(filexlsx.content)
                f.close()
            if re.search('2к', str(x)):
                f = open('file2.xlsx', 'wb')
                filexlsx = requests.get(x['href'])
                f.write(filexlsx.content)
                f.close()
            if re.search('3к', str(x)):
                f = open('file3.xlsx', 'wb')
                filexlsx = requests.get(x['href'])
                f.write(filexlsx.content)
                f.close()

    for n in range(1, 4):
        book = xlrd.open_workbook('file{}.xlsx'.format(n))
        sheet = book.sheet_by_index(0)

        num_cols = sheet.ncols
        num_rows = sheet.nrows

        groups_list = []
        groups = {}
        week_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        for col_index in range(num_cols):
            group_cell = str(sheet.cell(1, col_index).value)
            if re.search(r'\w{4}-\d\d-\d\d', group_cell):
                groups_list.append(group_cell)
                week = {'MON': None, 'TUE': None, 'WED': None, 'THU': None, 'FRI': None, 'SAT': None}
                for k in range(6):
                    day = [[], [], [], [], [], []]
                    for i in range(6):
                        for j in range(2):
                            subject = sheet.cell(3 + j + i * 2 + k * 12, col_index).value
                            lesson_type = sheet.cell(3 + j + i * 2 + k * 12, col_index + 1).value
                            lecturer = sheet.cell(3 + j + i * 2 + k * 12, col_index + 2).value
                            classroom = sheet.cell(3 + j + i * 2 + k * 12, col_index + 3).value
                            url = sheet.cell(3 + j + i * 2 + k * 12, col_index + 4).value
                            lesson = {'subject': subject, 'lesson_type': lesson_type, 'lecturer': lecturer,
                                      'classroom': classroom, 'url': url}
                            day[i].append(lesson)
                    week[week_days[k]] = day
                groups.update({group_cell: week})

        with open("groups{}.json".format(n), "w") as write_file:
            json.dump(groups, write_file)


def get_weather_from_site():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=...&units=metric',
        params={'lang': 'ru'})
    weather = json.loads(response.text)
    with open("weather.json", "w") as write_file:
        json.dump(weather, write_file)


def str_weather():
    with open('weather.json', 'r') as read_file:
        weather = json.load(read_file)
    str1 = 'Погода в Москве: '
    if 200 <= weather['weather'][0]['id'] <= 232:
        str1 += 'гроза\n'
    if 300 <= weather['weather'][0]['id'] <= 321:
        str1 += 'моросит\n'
    if 500 <= weather['weather'][0]['id'] <= 531:
        str1 += 'дождь\n'
    if 600 <= weather['weather'][0]['id'] <= 622:
        str1 += 'снег\n'
    if 700 <= weather['weather'][0]['id'] <= 781:
        str1 += weather['weather'][0]['description'] + '\n'
    if weather['weather'][0]['id'] == 800:
        str1 += 'ясно\n'
    if 801 <= weather['weather'][0]['id'] <= 804:
        str1 += 'облачно\n'
    str1 += weather['weather'][0]['description'][0].upper() + weather['weather'][0]['description'][1::] + ', '
    str1 += 'температура: ' + str(round(weather['main']['temp_min'])) + ' - ' + str(
        round(weather['main']['temp_max'])) + ' C\n'
    str1 += 'Давление: ' + str(weather['main']['pressure'] * 0.75) + ' мм рт. ст., влажность:' + str(
        weather['main']['humidity']) + '%\n'
    str1 += 'Ветер: '
    if 0 <= weather['wind']['speed'] <= 7.9:
        str1 += 'слабый, '
    if 8 <= weather['wind']['speed'] <= 17.1:
        str1 += 'сильный, '
    if weather['wind']['speed'] > 17.1:
        str1 += 'очень сильный, '
    str1 += str(weather['wind']['speed']) + ' м/с, '
    if 0 <= weather['wind']['deg'] <= 22.5 or weather['wind']['deg'] > 337.5:
        str1 += 'северный'
    if 22.5 < weather['wind']['deg'] <= 67.5:
        str1 += 'север-восточный'
    if 67.5 < weather['wind']['deg'] <= 112.5:
        str1 += 'восточный'
    if 112.5 < weather['wind']['deg'] <= 157.5:
        str1 += 'юго-восточный'
    if 157.5 < weather['wind']['deg'] <= 202.5:
        str1 += 'южный'
    if 202.5 < weather['wind']['deg'] <= 247.5:
        str1 += 'юго-западный'
    if 247.5 < weather['wind']['deg'] <= 292.5:
        str1 += 'западный'
    if 292.5 < weather['wind']['deg'] <= 337.5:
        str1 += 'северо-западный'
    return str1


def show_schedule_for_day(group, d):
    if d.weekday() == 6:
        return 'Занятий нет\n'
    course = -(int(group[-2::]) - 20)
    with open("groups{}.json".format(course), "r") as read_file:
        data = json.load(read_file)
    week_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    schedule = ''
    for i in range(6):
        str1 = str(i + 1) + ') '
        if data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['subject']:
            str1 += str(data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['subject']) + ', '
            if data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['lesson_type']:
                str1 += str(data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['lesson_type']) + ', '
            else:
                str1 += '--, '
            if data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['lecturer']:
                str1 += str(data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['lecturer']) + ', '
            else:
                str1 += '--, '
            if data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['classroom'] != 'Д':
                if data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['classroom']:
                    str1 += str(
                        data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['classroom']) + '\n'
                else:
                    str1 += '--\n'
            elif data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['url']:
                str1 += data[group][week_days[d.weekday()]][i][(d.isocalendar()[1] + 1) % 2]['url'] + '\n'
            else:
                str1 += '--\n'
        else:
            str1 += '--\n'
        schedule += str1
    return schedule


def show_schedule_for_week(group, d):
    d1 = d - datetime.timedelta(days=d.weekday())
    schedule = ''
    week_days = ['понедельник', 'вторник', 'среду', 'четверг', 'пятница', 'субботу']
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
              'декабря']
    for i in range(6):
        schedule += 'Расписание на ' + week_days[i] + ' ' + str(d1.day) + ' ' + months[d1.month - 1] + ':\n'
        schedule += show_schedule_for_day(group, d1)
        d1 += datetime.timedelta(days=1)
    return schedule


def show_schedule_for_day_on_week(group, ind):
    schedule = ''
    week_days = ['понедельник', 'вторник', 'среду', 'четверг', 'пятница', 'субботу']
    schedule += 'Расписание на ' + week_days[ind] + ' чётной недели:\n' + show_schedule_for_day(group,
                                                                                                datetime.date(2020, 5,
                                                                                                              11) + datetime.timedelta(
                                                                                                    days=ind))
    schedule += 'Расписание на ' + week_days[ind] + ' нечётной недели:\n' + show_schedule_for_day(group,
                                                                                                  datetime.date(2020, 5,
                                                                                                                11) + datetime.timedelta(
                                                                                                      days=ind + 7))
    return schedule


def main():
    vk_session = vk_api.VkApi(
        token='...')

    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    keyboard1 = VkKeyboard(one_time=True)
    keyboard1.add_button('на сегодня', color=VkKeyboardColor.POSITIVE)
    keyboard1.add_button('на завтра', color=VkKeyboardColor.NEGATIVE)
    keyboard1.add_line()
    keyboard1.add_button('на эту неделю', color=VkKeyboardColor.PRIMARY)
    keyboard1.add_button('на следующую неделю', color=VkKeyboardColor.PRIMARY)
    keyboard1.add_line()
    keyboard1.add_button('какая неделя?')
    keyboard1.add_button('какая группа?')

    users = {}
    week_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
              'декабря']

    get_schedule_from_mirea()
    get_weather_from_site()

    for event in longpoll.listen():
        if event.to_me and event.type == VkEventType.MESSAGE_NEW and (
                event.text.lower() == 'привет' or event.text.lower() == 'начать'):
            print('New from {}, text = {}'.format(event.user_id, event.text))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Введите номер группы один раз, чтобы я знал Вашу группу\nВведите "бот"(добавте номер группы или день недели для более точного результата),чтобы получить расписание\nВведите "погода",чтобы узнать погоду на сегодня в Москве'
            )

        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'погода':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message=str_weather()
            )

        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and re.search(r'\w{4}-\d\d-\d\d',
                                                                                 event.text) and len(
            event.text.split()) == 1:
            users[event.user_id] = event.text
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Я запомнил, что Вы из группы ' + event.text
            )

        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'бот' and len(
                event.text.split()) == 1:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Показать расписание группы ' + users[event.user_id],
                    keyboard=keyboard1.get_keyboard()
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and len(
                event.text.split()) == 2 and event.text.split()[0].lower() == 'бот' and event.text.split()[
            1].lower() in week_days:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=show_schedule_for_day_on_week(users[event.user_id], week_days.index(event.text.split()[1]))
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and len(
                event.text.split()) == 2 and event.text.split()[0].lower() == 'бот' and re.search(r'\w{4}-\d\d-\d\d',
                                                                                                  event.text):
            print('New from {}, text = {}'.format(event.user_id, event.text))
            users[event.user_id] = event.text.split()[1]
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Показать расписание группы ' + users[event.user_id],
                    keyboard=keyboard1.get_keyboard()
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and len(
                event.text.split()) == 3 and event.text.split()[0].lower() == 'бот' and event.text.split()[
            1].lower() in week_days and re.search(r'\w{4}-\d\d-\d\d', event.text):
            print('New from {}, text = {}'.format(event.user_id, event.text))
            users[event.user_id] = event.text.split()[2]
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=show_schedule_for_day_on_week(users[event.user_id], week_days.index(event.text.split()[1]))
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'на сегодня':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now()
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Расписписание на ' + str(d.day) + ' ' + months[
                        d.month - 1] + ':\n' + show_schedule_for_day(
                        users[event.user_id],
                        d)
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'на завтра':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now() + datetime.timedelta(days=1)
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Расписписание на ' + str(d.day) + ' ' + months[
                        d.month - 1] + ':\n' + show_schedule_for_day(
                        users[event.user_id],
                        d)
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'какая неделя?':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now()
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Идёт ' + str(d.isocalendar()[1] - 6) + ' неделя'
            )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'какая группа?':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now()
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Показываю расписание группы ' + users[event.user_id]
            )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'на эту неделю':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now()
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=show_schedule_for_week(users[event.user_id], d)
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me and event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'на следующую неделю':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            d = datetime.datetime.now() + datetime.timedelta(days=7)
            try:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=show_schedule_for_week(users[event.user_id], d)
                )
            except Exception:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Невозможно выполнить команду'
                )
        elif event.to_me:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Неизвестная команда'
            )


if __name__ == '__main__':
    main()
