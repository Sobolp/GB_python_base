"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
v_str = ''
v_from = 32
v_to = 127
v_elems = 0
for i in range(v_from, v_to + 1):
    if v_elems != 0:
        v_str += ' | '
    v_str += str(i) + '\t' + chr(i)
    v_elems += 1
    if v_elems == 10:
        print(v_str)
        v_str = ''
        v_elems = 0
print(v_str)