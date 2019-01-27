"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

a = ['A', '2']
b = ['C', '4', 'F']


def strArrToHexStr(strArr):
    hexStr = "0x"
    for i in strArr:
        hexStr += i
    return hexStr


def hexStrToInt(strArr):
    return int(strArrToHexStr(strArr), 16)


def hexToHexArr(hexStr):
    result = []
    for i in str(hexStr)[2::].upper():
        result.append(i)
    return result


print(hexToHexArr(hex(hexStrToInt(a) + hexStrToInt(b))))
print(hexToHexArr(hex(hexStrToInt(a) * hexStrToInt(b))))
