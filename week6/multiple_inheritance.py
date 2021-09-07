# 1) Виды наследования:
# В языке python есть 5 видов наследования

# -----------------------------------------------------------------------------------------------

# 1) Многоуровневое 

# Многоуровневое наследование - когда один класс наследуется от другого 
# класса, который наследуется от третьего класса,
# и получается множество уровней наследования 
# 
# class GrandParent:
#       pass

# class Parent(GrandParent):
#       pass 

# class Child(Parent):
#       pass 

# -------------------------------------------------------------------------------------------

# 2) Одиночное 

# Одиночное наследование - когда дочерний класс 
# наследуется от одного родительского класса 

# class Parent:
#       pass 
# class Child(Parent):
#       pass

# ---------------------------------------------------------------------------------

# 3) Иерархичесоке 

# Иерархическое наследование - когда более одного класса 
# является производным от одного базового класса 

# class Parent: 
#       pass
# class Child1(Parent):
#       pass
# class Child2(Parent):
#       pass
# class Child3(Parent):
#       pass



# -----------------------------------------------------------------------------------------------

# 4)Гибридное 

# Гибридное наследование - это смесь нескольких форм наследования

# class  GrandParent: 
#       pass

# class Parent1(GrandParent):
#       pass

# class Parent2:
#       pass

# class Child1(Parent1,Parent2):
#       pass

# class Child2(Parent2):
#       pass


# -----------------------------------------------------------------------------------------------

# 5) Множественное 

# Множественное наследование - когда дочерний класс 
# наследуется от нескольких родительских классов

# class Parent1: 
#       pass
# class Parent2:
#       pass
# class Child(Parent1,Parent2):
#       pass

# ---------------------------------------------------------------------------


# При множественном наследовании существуют более 
# одного родительского класса 

# MRO - Method Resolution Order - порядок решения методов 


# class Car:
#       def who(self):
#             print('i am iron man')
# class Child(Parent):
#       def who(self):
#             super().who()
#             print('paranoid')
# child = Child()
# child.who()
# 
# --------------------------------------------------------------------------------------------------

# Гибридное наследование

# class Grandpa:
#       def talant(self):
#             print('i am good at singing')
# class Grandma:
#       def talant(self):
#             print('i am good at dancing')

# class Father:
#       last_name = 'white'

#       def talant(self):
#             print('i am good at alcholism')

# class Mother(Grandma,Grandpa):
#       last_name = 'black'


# class Child(Mother,Father ):
#       last_name = 'white and black'

# child = Child()
# print(child.last_name)
# print(Child.mro())

# --------------------------------------------------------------------------------------------------


# class A: 
#       def __init__(self,param,param1):
#             print(f'hey, im class A , i got {param} {param1}')

# class B: 
#       def __init__(self,param):
#             print(f'hey, im class B , i got {param}')

# class C(A,B):
#       pass
#       # def __init__(self):
#       #       print(f'hey i do not get parametrs')

# c = C('makers', 'bootcamp')
# print(C.mro())


# --------------------------------------------------------------------------------------------------


# class All:
#       def say_hi(self):
#             print('hi')

# class A(All): 
#       def method1(self):
#             print('This is Method A')

# class B(All): 
#       def method2(self):
#             print('This is Method B')

# class C(A,B): 
#       def method3(self):
#             print('This is Method C')

# c = C()
# c.say_hi()


# --------------------------------------------------------------------------------------------------

class WheelsMixin:
      def __init__(self,wheels):
            self.wheels = wheels

class Radio:
      def play_music(self,music):
            print(f'you listen to {music}')


class Engine: 
      def __init__ (self,engine,volume):
            self.engine = engine
            self.volume = volume


class Oil:
      def __init__(self,oil):
            self.oil = oil

class Car(Oil,Engine,Radio,WheelsMixin): 
      def __init__(self,oil,engine,volume,type,wheels):
            # super().__init__(oil,engine,volume,wheels) 
            self.type = type
            self.wheels = wheels


class Boat(Oil,Engine,Radio):
      def __init__(self,oil,engine,volume,type):
            # super().__init__(oil,engine,volume,) 
            self.type = type 


class Ship(Oil,Engine,Radio): 
      def __init__(self,oil,engine,volume,type):
            # super().__init__(oil,engine,volume,) 
            self.type = type 


class Bike(Oil,Engine,Radio,WheelsMixin):
      def __init__(self,oil,engine,volume,type,wheels):
            super().__init__(oil,engine,volume,wheels) 
            self.type = type 
            self.wheels = wheels


car = Car('benz','V8',75,'19')
boat = Boat()
ship = Ship()
bike = Bike ()





# # class Person:
# #       def __init__(self,name,age):
# #             self.name = name 
# #             self.age = age
# #       def display(self):
# #             print(f'{self.name} {self.age}')
# # class Student(Person):
# #       def info (self,name,age,way):
# #             super().__init__(name,age)
# #             self.way = way 
# #       def display_student(self):
# #             print(f'{self.name} {self.age} {self.way}')

# # a = Student('asd''s','123')  
# # a. display_student()
# # a.display_student('sad')























