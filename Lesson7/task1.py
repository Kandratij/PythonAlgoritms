# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random


def bubble_sort(m):
    for i in range(len(m)):
        for j in range(len(m)-i-1):
            if m[j] < m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]


lst = [random.randint(-100,100) for i in range(100)]
print(lst)
bubble_sort(lst)
print(lst)