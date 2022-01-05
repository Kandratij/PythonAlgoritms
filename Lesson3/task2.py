#2. Во втором массиве сохранить индексы четных элементов первого массива.
#   Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
#   массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#   т.к. именно в этих позициях первого массива стоят четные числа.
import random
list1 = [random.randint(1,10) for i in range(10)]
list2 = [i for i in range(len(list1)) if list1[i] % 2 == 0]
print('Массив:',list1)
print('Индексы четных чисел:',list2)