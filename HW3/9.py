# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
rows = 4
columns = 10
maxLim = 100

matrix = []
minEl = [maxLim]*columns

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(random.randint(0, maxLim))
        print(row[j], end='\t')
        if row[j] < minEl[j]:
            minEl[j] = row[j]
    matrix.append(row)
    print()
print(minEl)

print('максимальный элемент среди минимальных элементов столбцов матрицы: %d' % max(minEl))

