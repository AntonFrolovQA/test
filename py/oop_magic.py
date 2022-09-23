# class Point:

#     color = 'red'
#     circle = 2

#     def __init__(self, a=0, b=0):
#         print("Вызов init")
#         self.x = a
#         self.y = b

#     def __del__(self):
#         print(f'Удаление экземпляра класса: {str(self)}')

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y

#     def get_coords(self):
#         return (self.x, self.y)


# pt = Point()
# print(pt.get_coords())
# ----------------------------------------------------------------------
# class Point:
    
#     def __new__(cls, *args, **kwargs):
#         print(f"Вызов __new__ для {str(cls)}")
#         return super().__new__(cls)
    
    
#     def __init__(self, x=0, y=0):
#         print(f"Вызов __init__ для {str(self)}")
#         self.x = x
#         self.y = y
# pt = Point(1, 2)


# ----------------------------------------------------------------------
# # Singleton
# class DataBase:
#     __instance = None

#     # def __call__(self, user):
#     #     self.user = user

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance

#     def __del__(self):
#         DataBase.__instance = None

#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
    
#     def connect(self):
#         print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")
    
#     def close(self):
#         print("Закрытие соединения с БД")

#     def  read(self):
#         return "данные из БД"
    
#     def write(self, data):
#         print(f"Запись в БД {data}")


# db = DataBase('admin', 'pass-1234', 80)
# db2 = DataBase('user1', 'pass-4567', 40)

# # print(id(db), id(db2))

# db.connect()
# db2.connect()


# ----------------------------------------------------------------------
# class Vector:
#     min_coord = 0
#     max_coord = 100

#     @classmethod
#     def validate(cls, arg):
#         return cls.min_coord <= arg <= cls.max_coord 


#     def __init__(self, x, y):
#         self.x = self.y = 0
#         # if Vector.validate(x) and Vector.validate(y):
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
        
#         print("---")
#         print(self.norm2(self.x, self.y + self.max_coord))
#         print("---")
            
    
#     def get_coord(self):
#         return self.x, self.y


#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y


# v = Vector(11, 22)
# print(Vector.norm2(33, 44))
# print(v.norm2(55, 66))


# coords = v.get_coord()
# print(coords) 
# print(Vector.validate(13))

# ----------------------------------------------------------------------
# class Point:
#     def __init__(self, x=0 , y=0):
#         self.__x = self.__y = 0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y

#     @classmethod
#     def __check_value(cls, x):
#         return type(x) in (int, float)

#     def set_coord(self, x,y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("Координаты должны быть числами")

#     def get_coord(self):
#         return self.__x, self.__y


# pt = Point(10, 20)
# pt.set_coord(11, 22)
# # print(pt.get_coord())
# # print(dir(pt))
# print(pt._Point__x)

# ---------------------
# from accessify import private, protected
# class Point:
#     def __init__(self, x=0 , y=0):
#         self.__x = self.__y = 0
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y


#     @private
#     @classmethod
#     def check_value(cls, x):
#         return type(x) in (int, float)

#     def set_coord(self, x,y):
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("Координаты должны быть числами")

#     def get_coord(self):
#         return self.__x, self.__y


# pt = Point(10, 20)
# pt.set_coord(11, 22)
# pt.check_value(5)
# ----------------------------------------------------------------------
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def set_coord(self, x, y):
#         if self.MAX_COORD <= x <= self.MIN_COORD:
#             self.x = x
#             self.y = y
    
#     @classmethod
#     def set_bound(cls, left):
#         cls.MIN_COORD = left

#     def __getattribute__(self, item):
#         if item == "x":
#             raise ValueError("доступ запрещен")
#         else:
#             return object.__getattribute__(self, item)

# pt1 = Point(10, 20)
# pt2 = Point(100, 200)

# a = pt1.y
# print(a)
# ----------------------------------------------------------------------
class Animal(object):
    pass


class Dog(Animal):
     def __init__(self, name):
        self.name = name
    

class Cat(Animal):
    def __init__(self, name):
        self.name = name



class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass



