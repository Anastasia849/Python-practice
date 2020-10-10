import re
import traceback


def change_time(str1):
    str1 = re.sub('[^:](([0-1][0-9])|([2][0-4])):[0-5][0-9](:[0-5][0-9])?[^:]', ' (TBD) ', str1)
    return str1


try:
    assert change_time('Уважаемые! Если вы к 09:00 не вернете чемода н, то уже в 09:00:69 я за себя не отвечаю.  PS. С временем 25:50 всё нормально!') == 'Уважаемые! Если вы к (TBD) не вернете чемода н, то уже в 09:00:69 я за себя не отвечаю.  PS. С временем 25:50 всё нормально!'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

