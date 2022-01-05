#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
num = int(input('Ведите целое число:'))
"""
Решение 1: цикл while
"""
n = num
r = 0
while n > 0 :
    r = r*10+n%10
    n //=10
print(r)

"""
Решение 2: Рекурсия
"""
def revers(a,b=0):
    if a//10:
        return revers(a//10,b*10+a%10)
    else:
        return b*10+a%10

print(revers(num))

"""
Решение 3: Реверс строки
"""
print(str(num)[::-1])