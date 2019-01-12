# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5                                               #   0101
b = 6                                               #   0110
print ("побитовая операция «И»: %d" % (a & b))      #   0100
print ("побитовая операция «ИЛИ»: %d" % (a | b))    #   0111
print ("побитовая операция «XOR»: %d" % (a ^ b))    #   0011
print ("побитовый сдвиг вправо: %d" % (a >> 2 ))    #   0001
print ("побитовый сдвиг влево: %d" % (a << 2 ))     #  10100