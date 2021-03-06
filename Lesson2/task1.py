# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
#   Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
#   а должна запрашивать новые данные для вычислений.
#   Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
#   Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему
#   об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
#   если он ввел 0 в качестве делителя.
def calc(x, y, sign):
    val = 0
    if sign == '+':
        val = x + y
    elif sign == '-':
        val = x - y
    elif sign == '*':
        val = x * y
    elif sign == '/':
        val = x / y
    return val


while True:
    while True:
        s = input('Введите знак операции (0-для выхода):')
        if '0+-/*'.find(s) == -1:
            print('оператор должен быть "+","-","/","*" или 0')
        else:
            break
    if s == '0':
        print('Запрошен выход из калькулятора')
        break
    x = int(input('Введите первый операнд:'))
    y = int(input('Введите второй операнд:'))
    if s=='/' and y==0:
        print(f'\033[91mДелить на ноль нельзя\033[0m')
    else:
        print(f'{x}{s}{y}={calc(x, y, s)}')
