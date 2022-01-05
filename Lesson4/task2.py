# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Проанализировать скорость и сложность алгоритмов.
# Сложност алгоритмов :
#  первый - O(n^2) т.к. по сути 2 цикла
#  второй - O(n log log n) -для получения всех натуральных чисел на отрезке,
#  но плюс еще нахождение i-го числа на отрезке O(n).
# Для небольших значений первый алгоритм даже эффективнее т.к. для решета Эратосфена требуется расчитать все натураные
# числа на отрезке, а в первом случае достаточно получить i-е число, и дальше считать не надо
# для i=5
## Время выполнения: 1.0251998901367188e-05
## 11
## Время выполнения: 0.011812686920166016
## 11
# чем число больше тем более эффективный второй алгоритм
# для i=500
## Время выполнения: 0.3605194091796875
## 3571
## Время выполнения: 0.026297569274902344
## 3571
import time


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        finish_time = time.time()
        print('Время выполнения:', finish_time-start_time)
        return res
    return wrapper


@get_time
def without_eratosthenes(prime_id):
    i, n, d = 0, 2, 2
    while True:
        if n % d == 0:
            if n == d:
                i += 1
                if i == prime_id:
                    break
            n += 1
            d = 2
        else:
            d += 1
    return n


@get_time
def with_eratosthenes(prime_id):
    n = 10000
    sieve = list(range(n+1))
    sieve[1] = 0
    i = 2
    while i <= n:
        if sieve[i] != 0:
            j = i + i
            while j <= n:
                sieve[j] = 0
                j = j + i
        i += 1

    i, j = 2, 0
    while True:
        if sieve[i] != 0:
            j += 1
            if j == prime_id:
                break
        i += 1
    return sieve[i]


print(without_eratosthenes(500))
print(with_eratosthenes(500))
