# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import statistics as s

ent_count = int(input('Ведите кол-во предприятий:'))
ent_dict = {}
for i in range(ent_count):
    ent_name = input('Введите наименование предприятия:')
    profit = [0, 0, 0, 0]
    for q in range(4):
        profit[q] = int(input(f'прибыль за {q+1} квартал:'))
    ent_dict.update({ent_name:profit})

all_profit =[]
for ent_profit in list(ent_dict.values()):
    all_profit.extend(ent_profit)
all_avg = s.mean(all_profit)

print('Предприятия с прибылью выше среднего:')
print(*[ent for ent in ent_dict if s.mean(ent_dict[ent]) > all_avg], sep="; ")

print('Предприятия с прибылью ниже среднего:')
print(*[ent for ent in ent_dict if s.mean(ent_dict[ent]) < all_avg], sep="; ")

