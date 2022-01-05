# 8.Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def IsLeepYear(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if IsLeepYear(int(input('Введите год:'))):
    print('Высокосный год')
else:
    print(f'Не высокосный год')