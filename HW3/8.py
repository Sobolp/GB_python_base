"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
"""

rows = 4
columns = 4

matrix = []


for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input('Введите елемент № %d строки № %d' % (j, i))))
    matrix.append(row)

for i in range(rows):
    s = 0
    for j in range(columns):
        print(matrix[i][j], end='\t')
        s += matrix[i][j]
    print('|\t', s)

