# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print ("Введите три числа (flo1;flo2;flo3):")
flo1 = float(input("\tflo1 = "))
flo2 = float(input("\tflo2 = "))
flo3 = float(input("\tflo3 = "))

if flo2 < flo1 < flo3 or flo3 < flo1 < flo2:
    print('Среднее:', flo1)
elif flo1 < flo2 < flo3 or flo3 < flo2 < flo1:
    print('Среднее:', flo2)
else:
    print('Среднее:', flo3)