# Написать функцию very_even(number), которая определяет является ли число "очень четным".
# Однозначное число "очень четное", если оно четное. Числа больше 10 "очень четные",
# если сумма их цифр - "очень четное" число.
#
# Примеры:
# very_even(88) => False -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 нечетное
# very_even(222) => True -> 2 + 2 + 2 = 8 => 8 четное

import traceback


def very_even(number):
    sum1 = 1
    while sum1:
        sum1 = 0
        while number:
            sum1 += number % 10
            number = int(number / 10)
        if int(sum1 / 10) == 0:
            return sum1 % 2 == 0
        number = sum1
    return False


# Тесты
try:
    assert very_even(4) == True
    assert very_even(5) == False
    assert very_even(12) == False
    assert very_even(1234) == False
    assert very_even(7897) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
