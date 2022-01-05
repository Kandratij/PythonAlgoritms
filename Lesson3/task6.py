#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
rlist = [random.randint(1,100) for i in range(10)]
min_i = 0
max_i = 0

print('Исходный массив:', rlist)
for i in range(1,len(rlist)):
    if rlist[min_i]>rlist[i]:
        min_i=i
    if rlist[max_i]<rlist[i]:
        max_i=i

if max_i<min_i:
    s = sum(rlist[max_i+1:min_i])
else:
    s = sum(rlist[min_i+1:max_i])

print(f'Мin Idx:{min_i}, Max Idx:{max_i} Сумма между ними:{s}')

