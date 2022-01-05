# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def go(self, code, acc):
        self.left.go(code, acc + "0")
        self.right.go(code, acc + "1")


class Leaf(namedtuple("Node", ["char"])):
    def go(self, code, acc):
        code[self.char] = acc or "0"


def hff_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    print(heapq)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1+freq2, count, Node(left, right)))

        count += 1
    code = {}
    if h:
        [(_freq, count, root)] = h
        root.go(code, "")
    return code


def hff_decode(encoded, code):
    sx = ""
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx += dec_ch
                enc_ch = ""
                break
    return sx


s = 'Пользователи. Управление Пользователями и группами'
code = hff_encode(s)
encoded = "".join(code[symbol] for symbol in s)

print(encoded)
print(code)

print(hff_decode(encoded, code))