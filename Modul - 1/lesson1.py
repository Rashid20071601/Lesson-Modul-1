# Переменная name в которой находится строка
name = 'Rashid'

# Сложение строк с переменной-строкой
print('Hello, ' + name + '!')

# Дублируем строки с помощью умножения
print('Hello ' * 5)

# Вывод символов из переменной-строки с помощью индексации символов
# (Индексация символов начинается с 0)
print(name[0])

# (Последняя буква)
print(name[-1])

# (От индекса 0 до индекса 4(Не включительно))
print(name[0:4])

# (От индекса 0 до индекса 4, но с шагом 2(Шаг 1 по умолчанию))
print(name[0:4:2])

# (С начала строки, до конца строки с шагом 3)
print(name[::3])

# (Вывод строки в обратном порядке)
print(name[::-1])