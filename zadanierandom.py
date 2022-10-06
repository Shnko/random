from random import randint

spisok = []
summa1 = 0
summa2 = 0
for i in range(15):
    x = randint(-100, 100)
    if x == 0:
        while x == 0:
            x = randint(-100, 100)
    spisok.append(x)
print("Список рандомных чисел:", spisok)
for i in range(15):
    if spisok[i] > 0:
        summa1 = summa1 + spisok[i]
    else:
        summa2 = summa2 + spisok[i]
print("сумма положительных чисел =", summa1)
print("сумма отрицательных чисел =", summa2)