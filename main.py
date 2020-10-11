# coding=UTF-8
import sys
from itertools import permutations
# import pyperclip # Закомментьте эту строчку
try:
    sys.stdin = open('input.txt', encoding='UTF-8')
except:
    pass
input_formula = input()
# Следующие замены для тестирование, чтобы можно было ctrl + c ctrl + v :)
# input_formula = input_formula.replace('∨', '+')
# input_formula = input_formula.replace('¬', '-')
# input_formula = input_formula.replace('∧', '*')
# input_formula = input_formula.replace('≡', '==')
# input_formula = input_formula.replace('→', '=>')
formula = ''
i = 0
variables = set()
while i < len(input_formula):
    if input_formula[i].isalpha():
        formula += 'vals["{}"]'.format(input_formula[i]) # Позже у нас будет словарь vals из названия переменной в ее значение
        variables.add(input_formula[i])
    elif input_formula[i] == '=':
        if input_formula[i + 1] == '>':
            formula += '<='
        else:
            formula += '=='
        i += 1 # Обработали сразу два символа
    elif input_formula[i] == '*':
        formula += ' & ' # Приходится использовать уродские символы, так как приоритет <= больше приоритета and, что противоречит законам логики
    elif input_formula[i] == '+':
        formula += ' | '
    elif input_formula[i] == '-':
        formula += '1-' # ~ Нельзя использовать, так как ~1 = -2.
    else:
        formula += input_formula[i] # Скобочки
    i += 1
rows_cnt = int(input())
known_results = []
pos_unknown = []
for i in range(rows_cnt):
    known_results.append([])
    row = input().split()
    for j in range(len(row)):
        if row[j] == '?':
            known_results[i].append(-1)
            pos_unknown.append((i, j))
        else:
            known_results[i].append(int(row[j]))
difference_cnt = len(known_results[0]) - 1 - len(variables)
# Количество переменных по мнению таблицы - количество переменных в формуле (оказалось, в таблице их может быть больше, чем в формуле Pog)
if difference_cnt:
    avalible_variables = input().split() # Придется ввести какие могут быть переменные из задания
    for name in avalible_variables:
        if name not in variables:
            variables.add(name)
            formula += ' | (vals["{0}"] & ~vals["{0}"])'.format(name)
print(formula)
vals = dict()
for i in range(1 << len(pos_unknown)): # Пытаемся дозаполнить таблицу всеми возможными способами
    for pos in pos_unknown:
        known_results[pos[0]][pos[1]] = i & 1
        i >>= 1
    # Теперь нам надо проверить, что не будет повторяющихся строк
    s = set(tuple(el) for el in known_results)
    if len(s) != rows_cnt:
        continue
    for columns_perm in permutations(variables):
        # Пусть переменные были a, b, c, тогда он попробует: первый столбец - отвечает за а, второй за b, третий за c, потом acb итд...
        for row in known_results:
            for column in range(len(variables)):
                vals[columns_perm[column]] = row[column] # Значение column'овой переменной из перестановки становится равно известному значению
            if eval(formula) != row[-1]:
                break
        else:
            print(*columns_perm, sep='')
            # pyperclip.copy(''.join(columns_perm)) # И эту тоже
            for el in known_results:
                print(*el)