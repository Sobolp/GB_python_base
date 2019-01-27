# 4.	Определить, какое число в массиве встречается чаще всего.
import random
# a = [5, 0, 1, 10, 10, 4, 0, 9, 7, 9]
a = ([random.randint(0, 10) for i in range(10)])
print(a)

uniqueSet = list(set(a))
print(uniqueSet)

result = [0]*len(uniqueSet)

for i in range(0, len(a)):
    for j in range(0, len(uniqueSet)):
        if a[i] == uniqueSet[j]:
            result[j] += 1
print(result)

print('Ответ: чаще других ...')
for i in range(0, len(result)):
    if result[i] == max(result):
        print('\t%d встречается %d раз(а)' % (uniqueSet[i], result[i]))


