#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a,b,c =map(int,input('Введите 3 разных числа:').split(' '))
def avg3(a,b,c):
    if b < a < c or c < a < b:
        return a
    elif a < b < c or c < b < a:
        return b
    else:
        return c

print('Среднее:',avg3(a,b,c))