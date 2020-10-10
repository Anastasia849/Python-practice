import math


def z(x, y, a, b):
    res = math.log(x) + y ** x + (5 * math.pi + 4.25 * math.pow(x, 2)) / (
        math.sqrt(math.fabs(1 - 2 * y) + 5)) - math.pow((y - a * math.pow(b, 2)), 1 / 3)
    return res


def f(x, y):
    res = 2 * (math.sqrt(math.fabs(math.sin(2 * x) - math.pow(math.cos(y), 2))) / (
            (math.pow(x, 3) + math.pow(y, 3)) * 0.25)) + math.exp(2 * x)
    return res

print(f(1,2))