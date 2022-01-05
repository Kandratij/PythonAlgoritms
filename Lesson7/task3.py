# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def shaker_sort(m):
    l = 0
    r = len(m) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(l, r):
            if m[i] > m[i + 1]:
                m[i], m[i + 1] = m[i + 1], m[i]
                swapped = True
        if not swapped:
            break
        r -= 1
        swapped = False
        for i in range(r - 1, l - 1, -1):
            if m[i] > m[i + 1]:
                m[i], m[i + 1] = m[i + 1], m[i]
                swapped = True
        l += 1


M = 5

lst = [random.randint(1,100) for i in range(2*M+1)]
print(lst)
shaker_sort(lst)
print(lst)
print('Медиана:', lst[M])


