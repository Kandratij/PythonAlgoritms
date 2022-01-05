# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Проанализировать скорость и сложность алгоритмов.
# Алгоритмы перестановки цифр в числе
# Сложност алгоритмов одинакова O(n)
# но второй алгоритм с использованием рекурсии чуть медленее, так как активнее использует память (стек)
# для текущих констант:
#  Время выполнения первого: 9.469315767288208
#  Время выполнения второго: 11.28838849067688

import random
import time

MIN_RAND_VAL =1000000000
MAX_RAND_VAL =9999900000
ITERATION =1000000  # что бы почуствовать разницу во времени выполняем

def get_time(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()
        print('Время выполнения:', finish_time-start_time)
    return wrapper

def revers_while(a):
    n = a
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r

@ get_time
def repeat_revers_while():
    list_num = [random.randint(MIN_RAND_VAL, MAX_RAND_VAL) for i in range(ITERATION)]
    for num in list_num:
        revers_while(num)

def revers_recursion(a, b=0):
    if a // 10:
        return revers_recursion(a // 10, b * 10 + a % 10)
    else:
        return b * 10 + a % 10

@ get_time
def repeat_revers_recursion():
    list_num = [random.randint(MIN_RAND_VAL, MAX_RAND_VAL) for i in range(ITERATION)]
    for num in list_num:
        revers_recursion(num)

repeat_revers_while()

repeat_revers_recursion()






