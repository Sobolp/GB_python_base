"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


def trying(count, number):
    inp = int(input('Попытка №%d: ' % count))
    if count == 10 or inp == number:
        if inp == number:
            print('Верно!')
        print('загаданное число: %d' % number)
    else:
        if inp > number:
            print('загаданное число меньше чем %d' % inp)
        else:
            print('загаданное число больше чем %d' % inp)
        trying(count + 1, number)


trying(1, random.randint(0, 100))