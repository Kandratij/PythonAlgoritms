# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib


def str_cnt(s):

    ss = {}

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub not in ss:
                ss[sub] = 0

    for p in ss:
        patt_hash = hashlib.sha1(p.encode("utf-8")).hexdigest()
        for i in range(len(s) - len(p) + 1):
            subs_hash = hashlib.sha1(s[i:i + len(p)].encode("utf-8")).hexdigest()
            if subs_hash == patt_hash:
                ss[p] += 1

    return ss


s = input("Введите строку: ")
result = str_cnt(s)
print(result)
print(f"Количество подстрок {sum(x for x in result.values())}")
