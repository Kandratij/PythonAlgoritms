#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
n=int(input('Введите число:'))
s1=0
for i in range(n):
    s1=s1+i+1

s2=n*(n+1)/2
print(f'1+2+...+{n} ={s1}')
print(f'{n}*({n}+1)/2={s2}')