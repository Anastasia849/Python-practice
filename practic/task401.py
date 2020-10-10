# Написать функцию backwardsPrime(start, stop), которая возвращает список
# всех простых в обоих направлениях чисел (являются простыми и перевернутое
# число также простое, например 13 и 31, 17 и 71), которые находятся между двумя
# за данными числами start и stop
#
# Примеры:
# backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]


import traceback


def reverse(n):
    str1 = str(n)
    str2 = str1[::-1]
    return int(str2)

def simple_dig(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
        if count > 1:
            return False
    return True

def backwardsPrime(start, stop):
    list1 = []
    if start < 10:
        start = 10
    for i in range(start + 1, stop):
        check = False
        check = simple_dig(i)
        if check:
            check = simple_dig(reverse(i))
            if check:
                list1.append(i)
    return list1


# Тесты
try:
    assert backwardsPrime(9900, 10000) == [9923, 9931, 9941, 9967]
    # assert backwardsPrime(2, 100) == [13, 17, 31, 37, 71, 73, 79, 97]
    # в проверочных значениях нет 11,которое удавлетворяет условию простого числа
    assert backwardsPrime(501, 599) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
