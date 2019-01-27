"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sumNum(number):
    result = 0
    for i in number:
        result += int(i)
    return result


def theBiggest(prev, prev_sum):
    result = prev
    result_sum = prev_sum
    next_n = str(int(input('Натуральное число:')))
    next_sum = sumNum(next_n)
    if next_sum > prev_sum:
        result = next_n
        result_sum = next_sum
    if next_n == '0':
        print('Число %s наибольшее (суммa = %d)' % (result, result_sum))
    else:
        theBiggest(result, result_sum)


print('Для завершения наберите "0"')
theBiggest(0, 0)
