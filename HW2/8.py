"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
def calc(where, what):
    result = 0
    for ch in where:
        if ch == what:
            result += 1
    return result


find = str(int(input('Какую цифру ищим: ')))
all_n = int(input('Количество вводимых чисел: '))

all_result = 0
for i in range(1, all_n+1):
    number = str(int(input('Введите число №%d :' % i)))
    all_result += calc(number,find)

print('Итого: %d раз' % all_result)
