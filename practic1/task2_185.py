# Написать функцию vowel_2_index, которая заменяет все гласные (a, e, i, o, u)
# в заданной строке на число – порядковый номер буквы в строке
#
# Примеры:
# vowel_2_index("this is my string") ==> "th3s 6s my str15ng"

import traceback


def vowel_2_index(str1):
    t = 1
    for i in str1:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
            p = t
            if str1.index(i) + 1 >= 10:
                t -= 1
            str1 = str1.replace(i, str(str1.index(i) + p), 1)
    return str1


# Тесты
try:
    assert vowel_2_index("this is my string") == "th3s 6s my str15ng"
    assert vowel_2_index("Tomorrow is going to be raining") == "T2m4rr7w 10s g1415ng t20 b23 r2627n29ng"
    assert vowel_2_index("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
