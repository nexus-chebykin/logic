# logic
Вводите формулу в консоль \ создаете файл input.txt
Вводите количество строк в таблице истинности
Вводите таблицу, если неизвестно значение в ячейке, то ?
Если переменных в формуле меньше, чем в таблице, то дополнительно вводите переменные через пробел
Пример ввода:
((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
3
? 1	0	0	1
0	0	0	1	1
0	1	?	?	1
Или
((y => z) + (-x * w)) == (w == z)
3
? 1	0	0	1
0	0	0	1	1
0	1	?	?	1
Еще:
(¬z)∧x
8
0	0	0	0
0	0	1	1
0	1	0	0
0	1	1	1
1	0	0	0
1	0	1	0
1	1	0	0
1	1	1	0
x y z
