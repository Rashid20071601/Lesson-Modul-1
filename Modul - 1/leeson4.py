# Запрашиваем от пользователя ввести его имя
name = input('Enter your name: ')
print(f'Hello, {name}!')

# input является строкой
print(type(name))

# Преобразуем str в int
age = int(input('Enter your age: '))
print (age)
print(type(age))

# Переводим нижний регистр в верхний с помощью метода /.upper()/
print('привет, я строка в нижнем регистре!'.upper())

# Переводим верхний регистр в нижний с помощью метода /.lower()/
print('ПРИВЕТ, Я СТРОКА В ВЕРХНЕМ РЕГИСТРЕ!'.lower())

# Изменяем символы внутри строки с помощью метода /.replace(old, new)/
print('Привет, Rashid!'.replace('Привет', 'Hello'))