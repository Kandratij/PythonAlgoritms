#4. Написать программу, которая генерирует в указанных пользователем границах:
#   случайное целое число;
#   случайное вещественное число;
#   случайный символ.
#   Для каждого из трех случаев пользователь задает свои границы диапазона.
#   Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#   Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import random,randint
a,b =map(int,input('Введите два значение для генерации случайного целого числа:').split(' '))
if a<b:
    print(randint(a,b))
else:
    print(randint(b, a))

a,b =map(int,input('Введите два значение для генерации случайного вещественного числа:').split(' '))
if a<b:
    print(random()*(b-a)+a)
else:
    print(random()*(a-b)+b)

a,b =input('Введите два символа для генерации случайного символа:').split(' ')
if ord(a)<ord(b):
    print(chr(randint(ord(a), ord(b))))
else:
    print(chr(randint(ord(b), ord(a))))
