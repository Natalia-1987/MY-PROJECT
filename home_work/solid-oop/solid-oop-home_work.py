# Домашнее задание по ООП: "Person"
# Создайте класс "Person" с атрибутами "имя", "возраст" и "пол". Добавьте метод для вывода информации о человеке.

# Определение базового класса Person
class Person:
    # Метод __init__ є конструктором класу в Python
    # Конструктор класса Person, принимающий name, age, sex
    def __init__(self, name, age, gender):
        # Инициализация атрибутов name, age и sex значениями переданными в аргументах
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"{self.name} is {self.age} years old and he is {self.gender}")


person = Person("Mike", 21, "male")
person.print_info()


# Задание 2: Инкапсуляция для "Employee"
# 2. Создайте класс "Employee" с атрибутом "зарплата", инкапсулируйте его.
# Добавьте методы для ставки и получения зарплаты с учетом премии.

# Cоздаем класс Employee и наследуемся от Person :

class Employee(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self._salary = salary

    # _salary (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)

    def set_salary(self, new_salary):
        self._salary = new_salary

    def get_salary(self):
        return self._salary


employee = Employee("nick_name", 20, "W", 2000)
employee.set_salary(3500)
print(f"Зарплата работника {employee.name}: {employee.get_salary()}")


# Задание 3: Полиморфизм для "Student"

# 3. Давайте создадим два класса, например, "Student" и "Employee", оба из которых имеют метод "study".

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")


class Employee:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is learning for professional development.")


# Затем напишем функцию "study", которая будет принимать объект любого из этих классов, и вызывать метод "study".

def study_anyone(anyone):
    anyone.study()


student = Student("John")
employee = Employee("nick_name")

study_anyone(student)
study_anyone(employee)

# 4. Принцип единственной ответственности (Single Responsibility Principle, SRP):
# Описание: Каждый класс должен иметь только одну причину для изменения.
# Принцип единой ответственности гласит, что у каждого класса должна быть только одна «ответственность» и он не должен брать на себя другие обязанности.

############################################################################################################################
# Пример нарушения:

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def save_to_database(self, user_data):
#         # Логика сохранения пользователя в базе данных
#
#     def send_email(self, message):
#         # Логика отправки электронной почты

############################################################################################################################
# Задание: Разделите класс на два класса: один для работы с базой данных, другой для отправки электронной почты.

# Теперь каждый класс имеет только одну ответственность:
# Класс User отвечает только за данные пользователя
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


# Класс EDBRepository занимается работой с базой данных
class DBRepository:

    def save_to_database(self, user_data):
        # Логика сохранения пользователя в базе данных
        pass


# А класс EmailSender занимается отправкой электронной почты

class EmailSender:
    def send_email(self, message):
        # Логика отправки электронной почты
        pass




