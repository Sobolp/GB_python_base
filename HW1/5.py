# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
print("Введите две буквы (ch1;ch2):")
ch1 = input("\tch1 = ")
ch2 = input("\tch2 = ")

intCh1 = ord(ch1)
intCh2 = ord(ch2)

# т.к. не указан какой Алфавит использовать делаю только для латинского но принцип один

if (intCh1 >= 65) and (intCh1 < 91):
    placeCh1 = intCh1 - 64  # High case
elif (intCh1 >= 97) and (intCh1 < 123):
    placeCh1 = intCh1 - 96  # lower case

if (intCh2 >= 65) and (intCh2 < 91):
    placeCh2 = intCh2 - 64  # High case
elif (intCh2 >= 97) and (intCh2 < 123):
    placeCh2 = intCh2 - 96  # lower case

print("%s находится на  %d месте" % (ch1, placeCh1))
print("%s находится на  %d месте" % (ch2, placeCh2))
print("Между ними %d " % (abs((placeCh2 - placeCh1))))
