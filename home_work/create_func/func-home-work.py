# Создайте функцию greet, которая принимает один аргумент name.
# Функция должна вернуть строку приветствия: "Hello, [name]!

def greet(name):
    return "Hello, " + name + "!"


result = greet('Nick_name')
print(result)  # Вывод: "Привет, Nick_name!"

"""Проверка на положительное число"""


# Создайте функцию is_positive, которая принимает один аргумент number.
# Функция должна вернуть True, если число положительное, и False в противном случае.


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


result = is_positive(7)
print(result)  # Вывод: True

"""Функция с условиями"""
# Напишите функцию c использованием input, которая распечатает текст "hello world!"
# если при ее вызове вы передаете в качестве аргументов пустую строку, но если было передано имя, то выводить "hello имя!"


def print_name(name_):
    if name_ == "":
        return "hello world!"
    else:
        return "hello " + name_ + "!"


result = print_name(input("Введите имя: "))
print(result)
