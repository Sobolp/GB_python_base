"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict

companies = defaultdict(list)
n = int(input("Количество предприятий: "))
total = 0.0
for i in range(n):
    name = input(str(i+1) + "-е предприятие: ")
    s = 0.0
    for j in range(4):
        income = float(input("Прибыль за " + str(j+1) + "-й квартал: "))
        s += income
        companies[name].append(income)
    companies[name].append(s)
    total += s

moreAver = []
lessAver = []
for i in companies:
    # print(companies[i])
    if companies[i][4] > total / n:
        moreAver.append(i)
    elif companies[i][4] < total / n:
        lessAver.append(i)

print("предприятия, чья прибыль выше среднего: ")
for p in moreAver:
    print("\t %s (Годовая прибыль: %d)" % (p, companies[p][4]))

print("предприятия, чья прибыль ниже среднего: ")
for p in lessAver:
    print("\t %s (Годовая прибыль: %d)" % (p, companies[p][4]))




