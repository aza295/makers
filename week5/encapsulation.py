                  # ИНКАПСУЛЯЦИЯ

# Приватные 
# Защищеннные  мы еще можем получить скрытыте данные
# так же наследуются в дочерних классах 
# Публиные 

# class A:
#       def _say_hello(self):
#             print('Hello world')

# class B(A):
#       pass 

# b = B()
# b._say_hello()


# Приватные данные - это те,
# которые скрыты от внешнего воздействия.
# Подчеркиваются двумя __ нижними пробелами 

# self.__name = 'makers'

# Защищенные данные - данные,
# которые защищены от внешнего воздействия,
# но в языке python х все еще можно изменить извне.
# Подчеркивется одним _ нижними пробелами 

# self._name = 'makers'


# Публичные данные - это данные,
# которые доступны извне, 
# и свободно могут подвергаться внешним воздействиям 

# self.name = 'makers'
# --------------------------------------------------------------------------------


            # МОДИФИКАТОРЫ ДОСУТПА

# 1) public - password, get_info()
# 2) protected - _password, get_info()
# 3) private - __password, get_info()


# ---------------------------------------------------------------------------------------------

# class User:
#       def __init__(self,username,password):
#             self.username = username
#             self.__password = password

#       def get_password(self,username):
#             if self.username == username:
#                   return self.__password
#             else:
#                   return 'no, go away'

#       def set_password(self,old_password,new_password):
#             if self.__password == old_password:
#                   self.__password = new_password
#             else:
#                   return 'No, go away'

#       def __get_info(self):
#             print(f'Username {self.username}, password {self.__password}')

# user1 = User(username='makers123', password= 192717)
# print(user1.username)
# print(user1.get_password(username='makers123'))
# user1.set_password(old_password='192717',
#                   new_password='hello666')
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username='makers123'))





# ----------------------------------------------------------------

# class Divider: 
#       def __init__(self):
#             self.__divide_num = 2
#       @property  
#       def divider(self):
#             return self.__divide_num
#       @divider.setter
#       def divider(self,value):
#             if not value == 0:
#                   self.__divide_num = value 
#                   return 'succesfully changed divide number'

#             else: 
#                   return 'no, you are gay'


#       def divide(self,value):
#             return value / self.__divide_num 

# obj = Divider()
# print(obj.divider)
# print(obj.divide(14))
# obj.divider = 14
# print(obj.divider)




# -----------------------------------------------------------------------------------------------------

# class Person: 
#       def __init__(self,name,last_name):
#             self.name = name
#             self.last_name = last_name
#       @property   
#       def full_name(self):
#             return f"{self.name} {self.last_name}"

# person = Person(name='Gordon' ,last_name= 'Matthew')
# print(person.full_name)

# ------------------------------------------------------------------------------------



# class Car:

#       def _inject_fuel(self):
#             print('fuel injected ')
      
#       def _init_bang(self):
#             print('bang')


#       def _send_signal_to_ignition_system(self):
#             print('ignition started')
#             self._inject_fuel()
#             self._init_bang()

#       def _send_signal_to_pc(self):
#             print('Start')
#             self._send_signal_to_ignition_system()

#       def start_engine(self):
#             self._send_signal_to_pc()
            
# car = Car()
# car.start_engine()

# -------------------------------------------------------------------------------------------------------------


# ИНКАПСУЛЯЦИЯ 

# 1) Объеденение данных и функций, 
# которые работают с этими данными в один объект

# 2) Набор инструментов для сокрытия реализации объекта 

# ------------------------------------------------------------------------------------------------------

                        # МОДИФИКАТОРЫ ДОСТУПА





# public 


class A:
      a = 10  # публичный

      def method(self):
            pass











# protected

class B:
      _b = 17 # защищеный

      def method(self):
            pass





# private

class Car:
      __c = 120 # приватный 

      def method(self):
            pass






# -------------------------------------------------------------------------------------------


# class A:
#       atttr1 = 10  # публичный
#       _attr2 = 15
#       __attr3 = 30
#       def method(self):
#             pass

# class B(A):
#       pass 


# class A:

#       def __init__(self,value):
#             self.__attr1 = value 
#       # setter
#       def set_attr1(self,new_value):
#             self.__attr1 = new_value
#       # getter
#       def get_attr1(self):
#             return self.__attr1

# a1 = A(10)
# a.set_attr1(20)
# a.get_attr1()


class Car: 
      __speed = 0

      @property
      def speed (self):
            return self.__speed
            
      @speed.setter 
      def speed(self,new_speed):
            self.__speed = new_speed

car1 = Car()
car1.speed = 20
print(car1.speed)








# b1 = B()
# print(b1._A__attr3)
# b1.__attr3
# print(b1._attr2)














) Что такое декоратор в Python?

Декоратор — это функция, которая позволяет обернуть 
другую функцию для расширения её функциональности без 
непосредственного изменения её кода.

2) Как указать, что класс Elephant наследуется от класса Animal?
Elephant.class = Animal

Elephant.parent = Animal()

class Elephant(Animal)

class Animal(Elephant)

3) Как создать экземпляр класса А?
a = A

a = new A()

a = new A

a = A()

4) В каком методе класса А нужно объявить переменную b = 10, чтобы у всех экземпляров А был по умолчанию нестатичный атрибут b со значемнием 10?
__init__

A

__default__

__b__

5) Что будет выведено в консоль в результате выполнения следующего кода?

2

222

Данный код не выполнится

1

6) Что будет выведено на экран?

Test.__test

Test.0

0

AttributeError: type object 'Test' has no attribute '__test'

7) Что такое полиморфизм?
Ваш ответ
8) Функция определенная внутри класса называется - ...
операция

функция-класс

фабрика

метод

9) Когда вызывается метод init?
Сразу после создания экземпляра класса


10) Что такое инкапсуляция?

 2) Набор инструментов для сокрытия реализации объекта

11) Какие сущестуют модификаторы доступа в икапсуляции?

public

unsuccessfully

private

forbidden

protected

12) Какими литералами обозначаются модификаторы доступа в инкапсуляции Python?
public, __protected, _private

_public, __protected, __private

public, _protected, __private

public, _protected, ___private

13) Какие методы переходят дочерним классам при наследовании в Python?(вопрос связан с инкапсуляцией)
Наследуются все методы

Наследуются только public и private методы

Наследуются только protected и private методы

Наследуются только public и protected методы

Наследуются только public методы









