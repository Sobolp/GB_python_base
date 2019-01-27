#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = ([random.randint(-1000, 1000) for i in range(10)])
# a = [1, -1, 2, 5, -1, 5]
print(a)

minEl = min(a)
maxEl = max(a)
print(minEl,maxEl)
for i in range(0,len(a)):
    if a[i] == minEl:
        a[i] = maxEl
    elif a[i] == maxEl:
        a[i] = minEl

print(a)
