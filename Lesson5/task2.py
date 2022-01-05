# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

hex_list1 = list(input('Введите первое шестнадцатеричное число:').strip().upper())
hex_list2 = list(input('Введите второе шестнадцатеричное число:').strip().upper())

hex_digit = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_list2num(hex_list):
    m, x = 0, 0
    for h in reversed(hex_list):
        x += hex_digit.index(h) * 16**m
        m += 1
    return x


def num2hex_list(num):
    h = []
    while True:
        h.insert(0, hex_digit[num % 16])
        num //= 16
        if num == 0:
            break
    return h


if set(hex_list1).issubset(hex_digit) and set(hex_list2).issubset(hex_digit):
    print('Сумма: ', num2hex_list(hex_list2num(hex_list1)+hex_list2num(hex_list2)))
    print('произведение: ', num2hex_list(hex_list2num(hex_list1)*hex_list2num(hex_list2)))
else:
    print(f'ошибка в веденных числах. Есть не корректные символы: {hex_list1}; {hex_list2}')


