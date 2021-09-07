# Полиморфизм в объектно-ориентированном програмировании
# - это возможность обработки разных типов данных
# с помощью одной и той же функции или метода.


# a = 6 
# b = 9 

# print(a+b)

# c = '6'
# d = '9'
# print(d+c)

# f = [1,2,3]
# e = [4,5,6]
# print(f+e)


# dir()

# a = 'makers'
# b = 3 
# c = [True,'bootcamp',666]
# d= {'toxic':'city'}
# e = (6,7,8,9)
# f = {False,'makers',7,12,27}
# print(f'this is string method:{dir(a)}')
# print(f'this is integer method:{dir(b)}')
# print(f'this is list method:{dir(c)}')
# print(f'this is dictionary method:{dir(d)}')
# print(f'this is tuple method:{dir(e)}')
# print(f'this is set method:{dir(f)}')
# ------------------------------------------------------------------------

# Полиморфизм на примере встроенных методов

# pop ()-> list,dict,set 

# list_ = [3,4,5,6]
# dict_ = dict(a=1,b=2,c=3)
# set_ = {True,'makaers',19,27}

# list_.pop(1)
# dict_.pop('b')
# set_.pop()

# print(list_)
# print(dict_)
# print(set_)


# update()-> dict,set

# dict_ = dict(a=19,b=27,c=30)
# set_ = {'show','me','colors',666}

# dict_.update(d=33,e=44)
# set_.update({'of','your','life'})
# print(dict_)
# print(set_)

# -----------------------------------------------------------------------

# Использование полиморфизма в своих классах 
# class car:
#       def __init__(self,name):
#             self.name = name 
#       def go_by_car(self,destination):
#             print(f'{self.name} is going by car  to {destination} ')

# class ship:
#       def __init__(self,name):
#             self.name = name 
#       def go_by_ship(self,destination):
#             print(f'{self.name} is going by ship to {destination}')

# class Airplane:
#       def __init__(self,name):
#             self.name = name 
#       def fly_by_airplane(self,destination):
#             print(f'{self.name} is flying by airplane to {destination}')




# class car:
#       def __init__(self,name):
#             self.name = name 
#       def go(self,destination):
#             print(f'{self.name} is going by car  to {destination} ')

# class ship:
#       def __init__(self,name):
#             self.name = name 
#       def go(self,destination):
#             print(f'{self.name} is going by ship to {destination}')

# class Airplane:
#       def __init__(self,name):
#             self.name = name 
#       def go(self,destination):
#             print(f'{self.name} is flying by airplane to {destination}')

# class Train:
#       def __init__(self,name):
#             self.name = name 
#       def go(self,destination):
#             print(f'{self.name} is going by crazy train to {destination}')

# ----------------------------------------------------------------
# class InfoMixin:
#       def info(self):
#             my_class = (self.__class__.__name__)
#             print(f"i'm a {my_class}, named, {self.name},age {self.age}")

# class Cat(InfoMixin): 
#       def __init__(self,name,age):
#             self.name = name 
#             self.age = age 
      
#       def make_sound(self):
#             print('meow')

# class Dog(InfoMixin):
#       def __init__(self,name,age):
#             self.name = name 
#             self.age = age

#       def make_sound(self):
#             print("i'm gay")

# class Duck(InfoMixin):
#       def __init__(self,name,age):
#             self.name = name 
#             self.age = age 
      
#       def make_sound(info):
#             print('kwa kwa')
# ----------------------------------------------------------------------------------------------------------------------------


# class T1:
#       def __init__(self,iterable):
#             self.list = iterable 

#       def total (self):
#             return sum(self.list)
# class T2:
#       def __init__(self,iterable):
#             self.list = iterable

#       def total (self):
#             return len(self.list)

# t1 = T1([3,6,9,12,15,18,21,24,27,30])
# t2 = T2([3,6,9,12,15,18,21,24,27,30])
# print(t1.total())
# print(t2.total())




# class Dog:
#       def __init__(self,name): 
#             self.name = name 
#       def voice(self):
#             print('Гав')

# class Cat:
#       def __init__(self,name):
#             self.name = name 
#       def voice(self):
#             print('Мяу')   

# c = Cat('shrek','')

# d = Dog('Nurzhan')
# d.voice()

# def to_pet(animal):
#       animal.voice()

# for animal in (c,d):
#       to_pet(animal)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Полиморфизм - метод с одинаковым названием 
# может по-разному реализовываться в разных объектах

# a = 1
# b = 2

# print(a+b) #3

# a = '1'
# b = '2'

# print(a+b) #12

# a = [1]
# b = [2]

# print(a+b) #[1,2]


# Полиморфизм - возможность функции работать с объектами разных типов,
# если у них реализован определенный метод. 


# len() - возвращает длину контейнера (строки,списки,кортежи,словари, множества)


# a1 = 'string'
# a2 = [1,2,3,4,5]
# a3 = (1,2,3,4)
# a4 = {'a':1,'b':2,'c':3}
# print(len(a1)) #6
# print(len(a2)) #5
# print(len(a3)) #4
# print(len(a4)) #3



# class myclass: 
#       def __init__(self,languages):
#             self.languages = languages 

# class1 = myclass(['js','python','c++','c#','pascal'])
# print(len(class1.languages))

# def len(obj):
#       return obj.__len__()

# class int:
#       def __init__(self):
#             ...

#       def __str__(self):
#             return str(self.val)
            
# a1 = 1 
# print(str(a1))
# a2 = '2'
# a3 = [1,2,3,4]

# class A: 
#       pass
# a4 = A()

# print(a1)
# print(a2)
# print(a3)
# print(a4)



# class triangle:
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height 

#       def triangle_area(self):
#             return 0.5 *self.base*self.height

# class square:
#       def __init__(self,side):
#              self.side = side
             
#       def square_area(self):
#             return self**2 


# class circle:
#       def __init__(self,radius):
#             self.radius = radius
      
#       def circle_area(self):
#             return 3.14*self.radius **2
# cil = circle(10)

# def get_shape_area(shape):
#       if  type(shape) == square: 
#             return shape.square_area()
#       elif type (shape) == circle:
#             return shape.circle_area()
#       return shape.trangle_area 

# print(get_shape_area(cil))




# class triangle:
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height 

#       def area(self):
#             return 0.5 *self.base*self.height

# class square:
#       def __init__(self,side):
#              self.side = side
             
#       def area(self):
#             return self**2 


# class circle:
#       def __init__(self,radius):
#             self.radius = radius
      
#       def area(self):
#             return 3.14*self.radius **2
# cil = circle(10)

# def get_shape_area(shape):
#       return shape.area
      

# print(get_shape_area())



# Абстрактный класс - класс, который имеет абстрактные методы

# абстрактные методы (класс,который нужно уточнить при наследовании)


# class Transport:
#       def move (self):
#             raise NotImplementedError('fsdf')
# class land_transport(Transport):
#       def move(self):
#             print('going on a land')

# tr1 = land_transport()
# tr1.move()


# from abc import ABC, abstractclassmethod

# class Transport(ABC):
#       @abstractclassmethod
#       def move(self):
#             pass 

# class Airtransport(Transport):
      
#       def move (self):
#             print('we are flying')

# obj1 = Airtransport()
# obj1.move()













