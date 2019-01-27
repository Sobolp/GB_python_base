"""
7.	В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
"""
import random
# a = [1, 0, 1, 4, 10, 4, 6, 9, 7, 9]
a = ([random.randint(0, 10) for i in range(10)])
print(a)
elMin1 = min(a)
indexMin1 = a.index(elMin1)

b = a[:]
b.remove(elMin1)

elMin2 = min(b)
if elMin1 != elMin2:
    indexMin2 = a.index(elMin2)
else:
    for i in range(0, len(a)):
        if elMin1 == a[i] and indexMin1 != i:
            indexMin2 = i
            break

print('Первый минимальный элемент %d по индексу %d' % (elMin1, indexMin1))
print('второй минимальный элемент %d по индексу %d' % (elMin2, indexMin2))


