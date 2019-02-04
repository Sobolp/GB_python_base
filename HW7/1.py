"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit

def bubbleSort(a):
    swapped = 0
    while swapped == 0 :
        swapped = -1
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                # print(a)
                swapped = 0
    return a

def bubbleSortImp(a):
    swapped = 0
    n = len(a)
    while swapped == 0:
        swapped = -1
        for i in range(1, n):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                # print(a)
                swapped = 0
        n -= 1
    return a

#ary = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]


n = int(input('Количество элементов: '))
ary = []
for i in range(n):
    ary.append( random.randint(-100, 100))
print(ary)
ary1 = ary[:]
# print(bubbleSort(ary))
# print(bubbleSortImp(ary1))
print(timeit.timeit("bubbleSort(ary)", setup="from __main__ import  bubbleSort, ary"))
print(timeit.timeit("bubbleSortImp(ary1)", setup="from __main__ import  bubbleSortImp, ary1"))

# Пример вызова:
# Количество элементов: 100
# [-87, -19, 59, -27, -41, 83, 94, -52, -42, 39, 64, 66, -92, 69, -38, -77, 21, -40, 8, -38, 21, -81, 95, -26, 47, 6, 41, 32, -48, 46, -37, 67, 2, 17, 36, -14, 65, -91, -29, -53, 99, -79, 93, 3, -8, -98, 50, -39, 10, -23, -99, 92, -65, -20, 23, -83, 74, -14, 7, -65, 2, 0, 18, 9, 25, -36, -79, -73, 98, -24, 46, -37, 76, 42, -81, 76, -53, 17, -10, 65, 98, -85, -75, -23, 53, 64, -36, 84, 52, 1, 92, 10, -45, 35, 8, 64, -60, 29, -75, 12]
# 7.126876069
# 6.886254212999999