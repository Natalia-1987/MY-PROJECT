"""Работа с целыми числами (int)"""
# ДЗ - 1:

# Определите переменную num1 со значением 15 и переменную num2 со значением 7.
# Выполните сложение, вычитание, умножение и деление переменных num1 и num2.
# Выведите результат каждой операции на экран.

# num1 = 15
# num2 = 7

num1 = 15
num2 = 7

print(f'Сума двух чисел: {num1 + num2}')
# або через створення окремої змінної, куди записується сума
sum = num1 + num2
print(f'Сума двух чисел: {sum}')

print(f'Різниця двух чисел: {num1 - num2}')
# або через створення окремої змінної, куди записується різниця
subtracting = num1 - num2
print(f'Різниця двух чисел: {subtracting}')

print(f'Добуток двух чисел: {num1 * num2}')
# або через створення окремої змінної, куди записується добуток
multiplying = num1 * num2
print(f'Добуток двух чисел: {multiplying}')

print(f'Частка двух чисел: {num1 / num2}')
# або через створення окремої змінної, куди записується частка
dividing = num1 / num2
print(f'Частка двух чисел: {dividing}')

"""Работа со строками (str)"""
# ДЗ - 2:

# Определите переменную name со значением "Name" и переменную surname со значением "Surname".
# Объедините строки в одну, разделив их пробелом.
# Выведите результат на экран.

# name = "Name"
# surname = "Surname"

name = "Name"
surname = "Surname"
# I вариант:
print(name + ' ' + surname)
# II вариант:
print(name, surname, sep=' ')

"""Работа с словарем (dict)"""
# ДЗ - 3:

# Определите словарь person с ключами "name", "age" и "city", и значениями "your_nick", 27  и "Kiev" соответственно.
# Выведите на экран все ключи словаря.
# Выведите на экран все значения словаря.

person = {'name': 'your_nick', 'age': '27', 'city': 'Kiev'}
keys = person.keys()
print(f'Все ключи словаря: {keys}')
values = person.values()
print(f'Все значения словаря: {values}')

"""Условные операторы"""
# ДЗ - 4:

# Определите переменную age со значением 22.
# Используя условный оператор (if-elif-else), выведите сообщение:
# "Вы совершеннолетний" если возраст больше или равен 18.
# "Вы несовершеннолетний" в противном случае.

age = 22
if age > 18:
    print("Вы совершеннолетний")
elif age == 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")

"""Циклы"""
# ДЗ - 5:

# Создайте список numbers от 1 до 5.
# Используя цикл for, выведите каждый элемент списка, умноженный на 2.

list_of_numbers = [1, 2, 3, 4, 5]
for i in list_of_numbers:
    print(i * 2)

"""Работа с числами и условиями"""
# ДЗ - 6:

# Определите переменную user_number со значением, введенным пользователем с клавиатуры (используйте функцию input).
# Проверьте, является ли введенное число четным. Выведите соответствующее сообщение.

user_number = int(input("Введите число: "))
if user_number % 2 == 0:
    print("Это чётное число")
else:
    print("Это нечётное число")

"""Создание и вызов функции"""


# ДЗ - 7:

# Создайте функцию calculate_square, которая принимает на вход сторону квадрата и возвращает его площадь.
# Вызовите функцию для квадрата со стороной 4 и выведите результат.


def calculate_square(a):
    return a ** 2


square = calculate_square(4)
print(f"Площадь квадрата: {square}")

"""Работа со списками и функциями"""


# ДЗ - 8:

# Создайте список numbers от 1 до 5.
# Создайте функцию square_numbers, которая принимает список чисел и возвращает список их квадратов.
# Вызовите функцию для списка numbers и выведите результат.


def square_numbers(numbers):
    return numbers ** 2


numbers_old = [1, 2, 3, 4, 5]
numbers_new = []
for item in numbers_old:
    new_item = square_numbers(item)
    numbers_new.append(new_item)

print(f"Список квадратов чисел: {numbers_new}")

"""Работа с функциями и строками"""
# ДЗ - 9:

# Создайте функцию reverse_string, которая принимает строку и возвращает ее в обратном порядке используйте срез.
# Вызовите функцию для строки "Python" и выведите результат.


def reverse_string(s):
    return s[::-1]


print(reverse_string("Python"))

"""Цикл for и оператор if"""
# ДЗ - 10:

# Создайте список чисел от 1 до 10 используя range.
# Используя цикл for и оператор if, выведите только те числа из списка, которые делятся на 2 без остатка.

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

