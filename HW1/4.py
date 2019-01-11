# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#   случайное целое число;
#   случайное вещественное число;
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

print ("Диапазон целых чисел (int1;int2):")
int1 = int(input("\tint1 = "))
int2 = int(input("\tint2 = "))
if int1 < int2:
    print (random.randint(int1, int2))
else:
    print(random.randint(int2, int1))

print ("Диапазон вещественных чисел (flo1;flo2):")
flo1 = float(input("\tflo1 = "))
flo2 = float(input("\tflo2 = "))
if flo1 < flo2:
    print (random.uniform(flo1, flo2))
else:
    print(random.uniform(flo2, flo1))

print ("Диапазон символов (ch1;ch2):")
ch1 = input("\tch1 = ")
ch2 = input("\tch2 = ")
if ch1 < ch2:
    print (chr(random.randrange(ord(ch1), ord(ch2))))
else:
    print(chr(random.randrange(ord(ch2), ord(ch1))))
