#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
rlist = [random.randint(1,1000) for i in range(10)]
min_i = 0
max_i = 0

print('до замены:', rlist)
for i in range(1,len(rlist)):
    if rlist[min_i]>rlist[i]:
        min_i=i
    elif rlist[max_i]<rlist[i]:
        max_i=i

print(f'Мin:{rlist[min_i]}, Max:{rlist[max_i]}')
n = rlist[min_i]
rlist[min_i] = rlist[max_i]
rlist[max_i] = n
print('после замены:', rlist)

