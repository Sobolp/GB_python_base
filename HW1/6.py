# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
print("Введите номер буквы :")
int1 = int(input("\tint1 = "))

# т.к. не указан какой Алфавит использовать делаю только для латинского но принцип один
# не делаю так же проверок на валидность входных данных

print("Это буква %s" % chr(int1 + 64))
