# instance method -> self

# Имеют доступ к экземпляру класса, так же и к классу
# (имеют доступ ко всем методам и атрибутам, которые определенный в классе).
# class A:
#       attr = 10 


#       def __init__(self,value):
#             self.attr2 = value 

#       def method1(self):
#             print(self.attr)
#             print(self.attr2)

# a = A(12)
# a.method1()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# class method -> @classmethod -> cls

# class методы имеют доступ только к атрибутам и методам класса

# class MyClass:
#       ac = 27

#       def __init__(self,value):
#             self.dc = value

#       @classmethod
#       def method2(cls):
#             print(cls.ac)
#             # print(cls.dc) #ERROR

# a = MyClass(20)
# a.method2()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# static method - @staticmethod 

# static методы - отдельная функция, которая не имеет досутпа ни к классу, 
# ни к его объектам
# Используются в случае, 
# если нужно добавить в класс логически определенную функцию 

# class A: 

#       @staticmethod 
#       def method1():
#             print('hello wolrd')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# class Makers:
#       language_choices = 'Python','JavaScript'


#       def __init__(self,name):
#             self.name = name 


#       def instance_method(self):
#             return f"hello, {self.name}"


#       @classmethod
#       def class_method(cls):
#             return f"welcome to makers what type of language you choose {cls.language_choices}"


#       @staticmethod
#       def static_method (choice):
#             return f"great! you choose {choice} course "

      
# student1 = Makers(name='lucas')
# print(student1.instance_method())
# print(student1.class_method())
# print(student1.static_method(choice='Python'))
# print()
# student2 = Makers(name='Rick')
# print(student2.instance_method())
# print(student2.class_method())
# print(student2.static_method(choice='JavaScript'))

# ------------------------------------------------------------------------------------------------------------------------
                        # classmethod


# class User:
#       def __init__(self,name,email):
#             self.name = name 
#             self.email = email 

#       def get_info(self):
#             return f"{self.name}, {self.email}"

#       @classmethod      
#       def add_data(cls,user_info:list):
#             name,email = user_info 
#             return cls(name,email)

# list_of_users = [
#       ['Emily','emi@yahoo.com'],
#       ['Bon Jovi', 'bon@gmail.com'],
#       ['Karen','ca@gmail.com']
# ]

# for info in list_of_users:
#       user = User.add_data(info)
#       print(user.get_info())

# ------------------------------------------------------------------------------------------------------------------------

                        # staticmethod

# class Lotery:
#       def __init__(self,name):
#             self.name = name 

#       @staticmethod
#       def _generate_number():
#             import random 
#             number = random.sample(list('123456789'),k=5)
#             number = ''.join(number)
#             return number
            

#       def get_number(self):
#             number = self._generate_number()
#             self.number = number 
#             return f'Dear {self.name}! Your lucky number is {self.number}'

# p1 = Lotery(name='lucas')
# print(p1.get_number())

# p2 = Lotery(name='luke')
# print(p1.get_number())


# ------------------------------------------------------------------------------------------------------------------------

# all types of methods



# class Pizza:

#       def __init__(self,ingridients:list):
#             self.ingridients = ingridients

#       def __repr__(self):
#             return f"Pizza with {self.ingridients}"

# pizza1 = Pizza(['tomatoes','mozarella','bazil'])
# pziza2 = Pizza(['meat','chili','cheese'])
# print(pizza1)
# print(pziza2)




# class Pizza:

#       def __init__(self,ingridients:list):
#             self.ingridients = ingridients

#       def __repr__(self):
#             return f"Pizza with {self.ingridients}"
      
#       @staticmethod
#       def circle_area(radius):
#             import math 
#             area = math.pi * radius ** 2
#             return f"Pizza's area is {area} cm2"      


#       def area(self,radius):
#             self.radius = radius
#             return self.circle_area(self.radius)

#       @classmethod
#       def margarita(cls):
#             return cls(['mozarella', 'tomatoes','basil'])


#       @classmethod
#       def pepperoni(cls):
#             return cls(['pepperoni', 'cheese'])


#       @classmethod
#       def chilli(cls):
#             return(['chilli peppers','cheese','souce'])

# pizza1 = Pizza.margarita()
# print(pizza1)
# print(pizza1.area(4))
# print('-------------------')
# pizza2 = Pizza.pepperoni()
# print(pizza1)
# print(pizza1.area(8))
# print('-------------------')
# pizza2 = Pizza.chilli()
# print(pizza1)
# print(pizza1.area(6))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# class User: 

#       def __new__(cls,*args,**kwargs):
#             email = args[0]

#             user = object.__new__(*args,**kwargs)
#             cls.send_mail(email)
#             return user 


#       def __init__(self,email,password):
#             self.e = email 
#             self.p = password

#       @staticmethod
#       def send_mail(email):
#             pass


# class A:
#       attr1 = 10 

#       def method1(self, new_value):
#             self.attr1 = new_value

#       @classmethod
#       def method2(cls,new_value):
#             cls.attr1 = new_value 

#       def method3(self,new_value):
#             self.__class__.attr1 = new_value

# a1 = A()
# a2 = A()
# a3 = A()

# a1.method1(20)
# a2.method2(30)
# a3.method3(25)
# print(a1.attr1)
# print(a2.attr1)
# print(a3.attr1)


# def add(x,y):
#       return x + y 
# def sub(x,y):
#       return x - y

# class Arithmetics:
#       @staticmethod
#       def add(x,y):
#             return x+y 

#       @staticmethod
#       def sub(x,y):
#             return x - y 


# dict.fromkeys(['a','b','c','d'])

# class User:
#       def __init__(self,username,password):
#             self.username = username
#             self.password = password 

#       def encrypt_password(self,raw_password):
#             from hashlib import md5
#             res = md5(raw_password.encode()).hexdigest()
#             return res 

# user1 = User('superstart','qwerty')
# print(user1.password)


username1 = 'user1'
username2 = 'user2'

pass1 = 'qwerty'
pass2 = 'qwerty'

from hashlib import sha512,pbkdf2_hmac

# hash1 = sha512((pass1+username1).encode()).hexdigest()
# hash2 = sha512((pass2+username2).encode()).hexdigest()

hash1 = pbkdf2_hmac('sha256',pass1.encode(),username1.encode(),100000)
hash2 = pbkdf2_hmac('sha256',pass1.encode(),username2.encode(),100000)

print(hash1)
print(hash2)


import hmac 
hmac.compare_digest(hash1,pbkdf2_hmac_hmac)
                  ('sha256',pass1.encode())


