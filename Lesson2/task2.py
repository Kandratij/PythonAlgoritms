#2. Посчитать четные и нечетные цифры введенного натурального числа.
#   Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
x=int(input('Введите число:'))
count_even = 0
count_odd = 0
while x > 0:
    if (x % 10) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    x = x // 10
print(f'Четных цифр {count_even}, нечетных {count_odd}')