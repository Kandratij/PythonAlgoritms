#7. По длинам трех отрезков, введенных пользователем, определить возможность
#   существования треугольника, составленного из этих отрезков.
#   Если такой треугольник существует, то определить, является ли он разносторонним,
#   равнобедренным или равносторонним.
a,b,c =map(int,input('Введите длины сторон треугольника:').split(' '))

if a+b>c and a+c>b and c+b>a:
    print(f'Треугольник со сторонами {a},{b},{c} существует')
    if a == b and b == c:
        print('и треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('и треугольник равнобедернный')
else:
    print(f'Треугольник со сторонами {a},{b},{c} не существует')cevvf k