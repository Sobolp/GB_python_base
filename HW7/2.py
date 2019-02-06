"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def mergeSort(a):
    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if len(left) > 0:
            result += left
        if len(right) > 0:
            result += right
        return result

    def merge_sort(l):
        if len(l) <= 1:
            return l
        left = []
        right = []
        for i in range(len(l)):
            if i < len(l) / 2:
                left.append(l[i])
            else:
                right.append(l[i])
        left = merge_sort(left)
        right = merge_sort(right)
        # print(left)
        # print(right)
        return merge(left, right)

    return merge_sort(a)


# ary = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]


n = int(input('Количество элементов: '))
ary = []
for i in range(n):
    ary.append(random.randint(0, 50))
print(ary)
print(mergeSort(ary))
