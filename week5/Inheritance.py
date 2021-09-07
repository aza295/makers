# # ТЕМА СЕГОДНЯШНЕГО УРОКА НАСЛЕДОВАНИЕ



# Основные принципы ООП:
# 1.Наследование - это наследование данных и функциональность некоторого существующего типа,
#     способствуя повторному использованию компонентов программного обеспечения.
# 2.Инкапсуляция - размещение в одном компоненте данных и методов, которые с ними работают.
# 3.Полиморфизм - способность функции обрабатывать данные разных типов.
# 4.Абстракция - это использование только тех характеристик объекта, которые с достаточной точностью представляют его в данной системе .
# 5.Композиция - более строгий вариант агрегирования, когда включаемый объект может существовать только как часть контейнера.
#     Если контейнер будет уничтожен, то и включённый объект тоже будет уничтожен






# class Table: # создание класса
#       places = 12  #  places = 12 это атрибуты класса

#       def __init__(self,width,length): # атрибуты экземпляров класса 
#             self.width = width  #
#             self.length = length #

# class CoffeeTable(Table):
#       places = 6 

#       def __init__(self,width,length,height):
#             Table.__init__(self,width,length)
#             self.height= height

# class OfficeTable(Table):
#       places = 1

#       def __init__(self,width,length,drawers):
#             Table.__init__(self,width,length)
#             self.drawers = drawers


# синтаксис
# class Parent:
#       pass 
# class Child(Parent):
#       pass




# class A:
#       pass

# class B(A):
#       pass

# class C(B):
#       pass 

# проверим является ли объект C(B): экземпляром класса  class A:

# c = B()
# print(isinstance(c,A))


# -----------------------------------------------------------------------



# Наследование методов и втрибутов 

# class Polygon:

#       sides = 'many'

#       def __init__(self,*args, **kwargs):
#             self.args = args 
#             self.kwargs = kwargs 
#             # print(self.args)
#             # print(self.kwargs)

#       def get_perimetr(self):
#             if self.args:
#                   return sum(self.args)
#             elif self.kwargs:
#                   return sum(self.kwargs.values())

# class Rectangle(Polygon):
#       sides = 4

#       def __init__(self,a,b):
#             self.a = a 
#             self.b = b


#       def get_perimetr(self):
#           return (self.a + self.b) *2 

# class Square(Rectangle):
      
#       def __init__(self, a):
#           self.a = a

#       def get_perimetr(self):
#           return self.a*4
# square = Square(a=55)
# print(square.sides)
# print(square.get_perimetr())


# class Triangle(Polygon):
#       sides = 3

#       def __init__(self,a,b,c):
#             self.a = a 
#             self.b = b
#             self.c = c
#       def get_perimetr(self):
#             return self.a * self.b * self.c 



# triangle1 = Triangle(a=8,b=8,c=8)
# print(triangle1.sides)
# print(triangle1.get_perimetr())

# rectangle = Rectangle(a=7,b=6)
# rectangle1 = Rectangle(a=27,b=19)
# print(rectangle.sides)
# print(rectangle.get_perimetr())
# print(rectangle1.get_perimetr())



# polygon = Polygon(a=19,b=19,c=19,d=19,e=19)

# print(polygon.get_perimetr())
# print(polygon.sides)

# ----------------------------------------------------------------


# Переопределение мотодов и атрибутов в дочерних классах

# class Mydict(dict):
#       def get(self,key,default = 'Feuer Frei!'):
#             print('this method has been changed')
#             return dict.get(self,key,default)

# dict1 = dict(a=3,b=5,c=7)
# print(dict1.get('a'))

# dict2 = Mydict(a=3,b=5,c=7)
# print(dict2.get('b'))

# super() function  возвращает все методы из родительского класса 
# class Human:
#       def __init__(self,name,last_name,id_number):
#             self.n = name 
#             self.l = last_name
#             self.id = id_number 


#       def get_info(self): # метод родительского класса 
#             print(f'{self.n} {self.l}\nid:{self.id}')
      
# class Employee(Human):
#       def __init__(self,name,last_name,id_number,position,salary):
#             super().__init__(name,last_name,id_number)
#             self.p = position
#             self.s = salary

#       def get_info(self):
#             super().get_info()
#             print(f'he works as {self.p}\n his salary is {self.s}')



# employee = Human(name='Edvard',last_name='Norton',id_number=295)
# employee.get_info()
# employee2 = Employee(name='Edvard',last_name='Norton',id_number=295,position='Actor',salary=2500000)
# employee2.get_info()


# ----------------------------------------------------------------------------------------------
# Наследование  (inheritance)

# Процесс когда один класс происходит от другого 

# Родительский класс или базовый
# class A:
#       pass 
# дочерний класс или производный 
# child,inherited
# class B:
#       pass 

# Дочерний класс перенимает все атрибуты и методы родительского класса, 
# при этом он так же может определять свои атрибуты и методы 


# class A: 
#     a = 10 
 
#     def method1(self): 
#         print('Assalamu aleikum musulmane') 
# class B(A): 
#     b = 12 
 
#     def methdo2(self): 
#         print('Ssaasasasdsad') 
 
# b1 = B() 
# print(b1.a) 
# print(b1.b) 
# b1.method1() 
# b1.methdo2()


# --------------------------------------------------------------------------------------

# Дочерние классы могут переопределять значения родительских классов,
#  а ак же поведение родительсикх методов 

# class A: 
#       a = 10 

# class B(A):
#       a = 15 

# class myclass:
#       def method1(self):
#             print('Hello world')

# class myclass1(myclass):
#       def method1(self):
#             print('punk')

# obj1 = myclass1()
# obj1.method1()




# Дочение классы могут не только переопределять методы 
# родителя но и дополнять их (расширять)

# super() - обращение к родительскому классу


# class A:
#       def method(self):
#             print('Goodbye world')

# class B(A):
#       def method(self):
#           print('i am iron man')
#           super().method1()
# b1 = B()
# b1.method1()



# class A:
#       attr1 = 10

#       def method1(self):
#             return self.attr1 **2 

# class B(A):
#       b = 15

#       def method1(self):
#             return super().method1() * self.b 

# b1 = B()
# print(b1.method1())

# OUTPUT: 1500
            
# --------------------------------------------------------------------------------

# Наследоваться можно и от встроенных объектов 


# class mystring(str):
#       def first(self):
#             return self[0]
#       def last(self):
#             return self[-1]

# my_string = mystring("AcDc")
# my_string.first()
# my_string.last()
# my_string.capitalize()


# a = [1,2,3,4]
# a[0]
# a[1]



# class Mylist(list):
#       def __getitem__(self,index):
#             if index <0:
#                   super().__getitem__(index)
#             elif index == 0 or index > len(self):
#                   raise IndexError('ты че дурак')
#             return super().__getitem__(index - 1)


# my_list = Mylist([1,2,3,4])
# print(my_list[0])



# a = {'a':1,'b':2}
# a.get('a')
# a.get('d')



# class mydict(dict):
#       def get(self,key,default='shabi, ni kaiwanxiao maf ?'):
#             return super().get(key, default)

# a1 = mydict({'a':1,'b':2})
# print(a1.get('d'))




# class animal:
#       pass

# class mammals(animal):
#       feeding = 'milk'

# class Cat(mammals):
#       foot_count = 4

# class Homecat(Cat):
#       pass 
# class wildcat(Cat):
#       pass

# class tigers(wildcat):
#       pass 

# class IndianTigers(tigers):



# множественное наследование 

# class A:
#       def Method1(self):
#           print('A!')

# class B(A):
#       def Method1(self):
#           print('B!')
      
# class C(B):
#       def Method1(self):
#           print('C!')
# class D(C):
#       def Method1(self):
#           print('D!')
# class E(D):
#       def Method1(self):
#           super().Method1()
#           print('E!')             
      
# e1 = E()
# e1.Method1()



class A:
      a = 10 
class B:
      a =15

class C(B,A):
      def get_a(self):
            print(self.a)


c1 = C()
c1.get_a()































