# 1.	В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
a = [0, 0]
result = [0]*10
print(result)
for i in range(2,100):
    for j in range(2,10):
        if i % j == 0:
            result [j] += 1

for i in range(2, 10):
    print('количиство чисел кратное %d: %d' % (i, result[i]))


