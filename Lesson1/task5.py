#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
a,b = input('Введите две буквы:').lower().split(' ')
print(f'"{a}" позиция {ord(a)-96}; "{b}" позиция {ord(b)-96}')
print(f'между ними находится {abs(ord(b)-ord(a))-1} букв(ы)')