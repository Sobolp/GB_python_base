"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


n = int(input('Введите любое натуральное число: '))
left = 0
for i in range(1, n+1):
    left += i
right = n * (n + 1) / 2

if left == right:
    print('1+2+...+n = n(n+1)/2 Верно!')
else:
    print('1+2+...+n = n(n+1)/2 Неверно!')

print('1+2+...+n = %d' % left)
print('n(n+1)/2 = %d' % right)
