# Задан список целых чисел. Написать функцию max_three_sum,
# которая возвращает максимальную сумму трех элементов без их повторов
#
# Пример:
# [1,8,3,4,0,8,4] ==> 15


import traceback


def max_three_sum(arr):
    for i in range(3):
        imax = i
        for j in range(i + 1, len(arr)):
            if arr[imax] < arr[j]:
                if i == 0 or i > 0 and arr[j] < arr[i - 1]:
                    imax = j
        arr[i], arr[imax] = arr[imax], arr[i]
    return arr[0]+arr[1]+arr[2]


# Тесты
try:
    assert max_three_sum([2, 1, 8, 0, 6, 4, 8, 6, 2, 4]) == 18
    assert max_three_sum([-13, -50, 57, 13, 67, -13, 57, 108, 67]) == 232
    assert max_three_sum([-2, -4, 0, -9, 2]) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
