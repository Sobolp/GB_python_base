# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

print("Введите год :")
year = int(input("\tyear = "))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Невисокосный")
else:
    print("Високосный")