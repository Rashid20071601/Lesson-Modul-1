# Создаем кортежи
tuple_1 = 1, 2, 3, True, 'String'
tuple_2 = (1 ,2, 3, True, 'String')
tuple_3 = tuple([1, 2, 3, True, 'String'])
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(type(tuple_1), type(tuple_2), type(tuple_3))

# Особенности кортежей:
# 1 - Не изменяемость
# 2 - Упорядоченность
# 3 - Элементы, хранящиеся внутри, кортежей могут быть разных типов

# Обращаемся к элементу кортежа по индексу
print(tuple_1[4])

# Проверяем размер в памяти с помощью команды / .__sizeof__() /
print(tuple_1.__sizeof__())

# Изменяем список внутри кортежа
tuple_4 = [1, 2, 3, 'str', True], 4, 'Rashid', False
print(tuple_4)
tuple_4[0][3] = 'String'
print(tuple_4)

# Прибавляем кортеж к другому
tuple_5 = 1, 2, 3, 4
tuple_6 = 5, 6, 7, 8
tuple_7 = tuple_5 + tuple_6
print(tuple_7)

# Умножаем кортеж
tuple_8 = 1, 2, 3
print(tuple_8 * 3)