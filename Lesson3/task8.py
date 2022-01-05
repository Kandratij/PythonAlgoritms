#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
lines = 5
columns = 4
m = [i[:] for i in [[0] * columns] * lines]
for i in range(lines):
    for j in range (columns-1):
        m[i][j]=int(input(f'[{i}][{j}] = '))
        m[i][columns-1] += m[i][j]

for i in range(lines):
    s = ', '.join([str(l).rjust(5) for l in m[i]])
    print(s)


