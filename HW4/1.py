"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
 в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


# 3.	Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
#  то надо вывести число 6843.

import timeit


def reversed(s):
    # print(s)
    if len(s) == 2:
        return s[-1] + s[0]

    if len(s) == 1:
        return s[0]

    return s[-1] + reversed(s[1:len(s) - 1]) + s[0]

def reverseList(s):
    b = []
    b = [i for i in s]
    b.reverse()
    return b

a = str(int(input('Введите натуральное число: ')))
# print(reversed(a))
# print(reverseList(a))
# print(a[::-1])


print(timeit.timeit("a[::-1]", setup="from __main__ import  a"))

print(timeit.timeit("reversed(a)", setup="from __main__ import reversed, a"))

print(timeit.timeit("reverseList(a)", setup="from __main__ import reverseList, a"))

# пример вызова:
# Введите натуральное число: 123454536475687698789
# 0.1433178470000005
# 5.119558542
# 0.7746626140000004
