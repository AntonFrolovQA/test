from math import pi

# -------------------------------------------------
# Инкапсуляция
# -------------------------------------------------
def incapsulation():
    class Person:
        def __init__(self, name):
            self.__name = name
            self.__age = 1
        
        def set_age(self, age):
            if 1 < age < 110:
                self.__age = age
            else:
                print("AGE --- Invalid  Value")

        def get_name(self):
            return self.__name
        
        def get_age(self):
            return self.__age
        
        def display_info(self):
            print(f"Name: {self.__name}\nAge: {self.__age}")
    tom = Person("Tom")
    tom.display_info()
    tom.set_age(-100)
    tom.set_age(28)
    tom.display_info()
# -------------------------------------------------
# Аннотации свойств (setter, getter)
# -------------------------------------------------
def annotation():
    class Person:
        def __init__(self, name):
            self.__name = name
            self.__age = 1

        @property
        def age(self):
            return self.__age
        
        @age.setter
        def age(self, age):

            if 1 < age < 110:
                self.__age = age
            else:
                print("Invvalid value, insert amount 1-110")
        
        @property
        def name(self):
            return self.__name
        
        def display_info(self):
            print(f"Name: {self.__name}, Age: {self.__age}")

    tom = Person("Tom")
    tom.display_info()
    tom.age = -100
    print(tom.age)
    tom.age = 28
    tom.display_info()
# -------------------------------------------------
# Наследование
# -------------------------------------------------
def legacy():
    class Person:
        def __init__(self, name):
            self.__name = name
        
        @property
        def name(self):
            return self.__name
        
        def display_info(self):
            print(f"Name: {self.name}")
    class Employee(Person):
        
        def work(self):
            print(f"{self.name} works")
    
    tom = Employee("Tom")
    print(tom.name)
    tom.display_info()
    tom.work()
# -------------------------------------------------
# Множественное наследование
# -------------------------------------------------
def multy_legacy():

    class Employee:

        def __init__(self, name):
            self.__name = name

        @property
        def name(self):
            return self.__name
        
        def work(self):
            print(f"{self.name} works")
    class Student:

        def __init__(self, name):
            self.__name = name

        @property
        def name(self):
            return self.__name

        def study(self):
            print(f"{self.name} studies")
    class WorkingStudent(Employee, Student):
        pass
    tom = WorkingStudent("Tom")
    tom.work()
    tom.study()
# -------------------------------------------------
# Переопределение функционала базового класса
# ------------------------------------------------- 
def re_func():
    class Person:
        def __init__(self, name):
            self.__name = name

        @property
        def name(self):
            return self.__name

        def display_info(self):
            print(f"Name: {self.__name}")
    
    class Emplyee(Person):
        
        def __init__(self, name, company):
            super().__init__(name)
            self.company = company

        def display_info(self):
            super().display_info()
            print(f"Company: {self.company}")

        def work(self):
            print(f"{self.name} works")
    tom = Emplyee("tom", "Microsoft")
    tom.display_info()
    tom.work()
# -------------------------------------------------
# Проверка типа объекта
# ------------------------------------------------- 
def data_type():
    class Person():

        def __init__(self, name):
            self.__name = name

        @property
        def name(self):
            return self.__name

        def do_nothing(self):
            print(f"{self.name} does nothing")

    # класс работника
    class Employee(Person):

        def work(self):
            print(f"{self.name} works")

    # класс студента
    class Student(Person):
        def study(self):
            print(f"{self.name} studies")


    def act(human):
        if isinstance(human, Student):
            human.study()
        elif isinstance(human, Employee):
            human.work()
        elif isinstance(human, Person):
            human.do_nothing()

    tom = Employee('Tom')
    bob = Student('Bob')
    sam = Person('Sam')

    act(tom)
    act(bob)
    act(sam)
# -------------------------------------------------
# Атрибуты классоа
# -------------------------------------------------
def attrib():

    class Person_01:
        type = "Person"
        description = "Describes a person"

    print("type: " + Person_01.type)
    print("description: " + Person_01.description)

    Person_01.type = "Class Person"
    print("changing type to: " + Person_01.type)


    class Person_02:
        type = "Person"
        def __init__(self, name):
            self.name = name
    
    tom = Person_02("Tom")
    bob = Person_02("Bob")

    print(tom.type)
    print(bob.type)

    Person_02.type = "Class Person"
    print(tom.type)
    print(bob.type)


    class Person_03:
        default_name = "Undefined"

        def __init__(self, name):
            if name:
                self.name = name
            else:
                self.name = Person_03.default_name

    tom = Person_03("Tom")
    bob = Person_03("")
    print(tom.name)
    print(bob.name)


    class Person_04:
        name = "Undefined"

        def print_name(self):
            print(self.name)
        
    tom = Person_04()
    bob = Person_04()
    tom.print_name()
    bob.print_name()
# -------------------------------------------------
# Статические методы
# -------------------------------------------------
def static():
    class Cylinder:

        @staticmethod
        def make_area(d, h):
            circle = pi * d ** 2/4
            side = pi * d * h
            return round(circle*2 + side, 2)

        def __init__(self, di, hi):
            self.di = di
            self.hi = hi
            self.area = self.make_area(di, hi)
    a = Cylinder(1, 2)

    print(a.area)
    print(a.make_area(2, 2))
# -------------------------------------------------




