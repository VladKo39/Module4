'''
''
Домашняя работа по уроку "Модули и пакеты"
Цель: закрепить навык создания и импортирования модулей, а так же функций и переменных находящихся в них.

Задача "А как делить?":
Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление,
но разными способами.
Пример результата выполнения программы:
Исходный код (названия функций могут быть другими):
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
Вывод на консоль:
23.0
Ошибка
7.0
inf
'''
from fake_math import divide as d_f
from true_math import divide as d_t
result1 = d_f(69, 3)
result2 = d_f(3, 0)
result3 = d_t(49, 7)
result4 = d_t(15, 0)
print(f'Результат1 module_4_1:   {result1}')
print(f'Результат2 module_4_1:   {result2}')
print(f'Результат3 module_4_1:   {result3}')
print(f'Результат4 module_4_1:   {result4}')
