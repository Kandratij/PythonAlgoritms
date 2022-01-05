# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
import time


def merge_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return lst
    llst = lst[:len(lst) // 2]
    rlst = lst[len(lst) // 2:]
    merge_sort(llst)
    merge_sort(rlst)
    l = r = t = 0
    tmp = [0] * len(lst)
    while l < len(llst) and r < len(rlst):
        if llst[l] <= rlst[r]:
            tmp[t] = llst[l]
            l += 1
        else:
            tmp[t] = rlst[r]
            r += 1
        t += 1
    while l < len(llst):
        tmp[t] = llst[l]
        l += 1
        t += 1
    while r < len(rlst):
        tmp[t] = rlst[r]
        r += 1
        t += 1
    for i in range(len(lst)):
        lst[i] = tmp[i]



lst = [round(random.uniform(1.0,50.0),3) for i in range(50)]
print(lst)
start_time = time.time()
merge_sort(lst)
print('Время выполнения:', time.time()-start_time)
print(lst)