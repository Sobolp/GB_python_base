"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def pow2(s):
    result = 1
    for i in range(0, s):
        result *= 2
    return result


n = int(input('Количество элементов: '))

result = 0.0
sign = 1
for i in range(0, n):
    if i % 2 != 0:
        sign = -1
    else:
        sign = 1
    next_el = 1 / pow2(i) * sign
    result += next_el

print('Сумма равна: %f' % result)
