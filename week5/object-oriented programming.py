# Парадигма(пример,модель,образец)
# (ООП) - Объектно-ориентированное програмирование - парадигма програмированния,
# в которой основными концепциями являются понятия объектов и классов


# Класс - тип,описывающий устройство объектов.Объект - это экземпляр
# класса. Класс можно сравнить с чертежом, по которому создаются объекты

# В python все является объектами - и строки,списки,словари и все остальное.  

# Класс это способ описания объектов, какие характеристики у объекта(атрибуты), 
# какие действия он может выполнять(методы)



# class A:
#       pass 

# a = A() # Экземпляр класса,объект класса instance,object 
# print(isinstance(a,A))

# class int:
#       # свойства 
#       pass
# class str:
#       # свойства
#       pass
# class list:
#       pass
#       # свойства

# a = 4
# print(type(int))


# Встроенные типы данных 

# int, str, list, tuple, dict, bool, set, frozenset

# a = 5
# print(type(a))


# ---------------------------------------------------------------------------------------
# СОЗДАНИЕ КЛАССА 


# class Recatangle:
#       def __init__(self,width,lenghth):
#           self.w = width
#           self.l = lenghth
#       def area(self):
#             return self.w*self.l

# rec1 = Recatangle(4,6)
# rec2 = Recatangle(2,7)
# print(rec2.area())






# class person: # вызываем класс
#       def __init__(self,*args): #
#           self.c = args # 

#       def cat(self): #
#             return self.c#





# 1)
# class car:
#       def __init__(self, *args):
#             self.a = args 
#       def chr(self):
#             return self.a
# u = car('name=BMW','model=750','year=1998','country=German')
# print(u.chr())


# 2)
# class car:
#       def __init__(self,name,model,year,country):
#             self.a = name
#             self.b = model
#             self.c = year
#             self.d =  country
#       def chr(self):
#             return self.a,self.b,self.c,self.d
            
# u = car('BMW','750','1998','German')
# print(u.chr())

# 3)
# class Recatangle:
#       def __init__(self,width,lenghth):
#           self.w = width
#           self.l = lenghth
#       def area(self):
#             return self.w*self.l

# rec1 = Recatangle(4,6)
# rec2 = Recatangle(2,7)
# print(rec2.area())
# ----------------------------------------------------------------------------------------







# под вопросом 
# class Person: 
#     def __init__(self, name, last_name, id_number): 
#         self.name = name 
#         self.lastname = last_name 
#         self.id = id_number 
     
#     def get_info(self): 
#         print(f'{self.name} {self.lastname}, id: {self.id}') 
 
# class Employee(Person): 
#     def __init__(self, name, last_name, id_number, position, salary): 
#         Person.__init__(self, name, last_name, id_number) 
#         self.position = position 
#         self.salary = salary 
     
#     def get_info(self): 
#         Person.get_info(self) 
#         print(f'He works as {self.position} and his salary is {self.salary}') 
 
# employee = Employee(name='English', last_name='Man', 
#                     id_number=228, position='transaltor', 
#                     salary= 1969) 
# employee.get_info()

# -------------------------------------------------------------------------------------


# class myclass:
#       a = 10 # 10 is atribute 
#       def method(self): #method
#             pass


# a = 'abc'
# a.capitalize()

# class str:
#       def capitalize(self):
#             pass



# Класс это способ описания объектов, какие характеристики у объекта(атрибуты), 
# какие действия он может выполнять(методы)

# class Student: 
#       course = 5 # atributes of class

#       def __init__(self,name,last_name,age):
#             self.n = name 
#             self.l = last_name 
#             self.a = age
#       # атрибуты экземпляра
#       def get_profile(self):
#             return f'{self.n},{self.l},{self.a} годa,{self.course} курс Политех'
      
#       # name = 'James' # атрибуты 
#       # last_name = 'Heatfield' # атрибуты 
#       # age = 25 #  атрибуты 

#       def sleep(self):
#             print('sleep during the lesson')

# student1 = Student('James','Heatfield',25)
# student2 = Student('Dave','Mustaine',24)

# print(student2.get_profile())

# OUTPUT: Dave,Mustaine,24 годa,5 курс Политех

# ----------------------------------------------------------

# class Patient:
#       def __init__(self,name,last_name,age,weight,height):
#             pass

# class Client:
#       def __init__(self,name,last_name,date_of_birth,passport):
#           pass

# class Customer: 
#       def __init__(self,name, age, phone_num):
#           pass

# Принцип абстрагирования 


# class Notebooks:
#       def __init__(self,color,screen,cpu,ram,hdd,ssd):
#           pass


# class Notebooks:
#       def __init__(self,brand,model,price,chr,):
#           pass

# class Engine:
#       def __init__(self,fuel,volume,power):
#             self.f= fuel
#             self.v= volume
#             self.p=power
# engine1 = Engine('diesel',6,500)


# class car:
#       brand = 'Toyota'

#       def __init__(self,model,color,volume,engine,interior,price):
#           self.m = model
#           self.c = color
#           self.e = engine
#           self.i = interior
#           self.p = price

# car1 = car('Tundra','Black',engine1,'benzin','leather',1690000)
# print(car1.)


# ----------------------------------------------------------------------------------------

# class product:
#       '''Класс, описывающий продукты.
#       принимает название проукты и цену'''
#       def __init__(self,title,price):
#             self.title = title
#             self.price = price
#       def __str__(self):
#             return self.title
            
# product1 = product(title='apple iphone 12',price=120000)
# product2 = product(title='apple macbook',price=180000)
# product3 = product(title='Samsung galaxy s 21',price= 100000)

# class User:
#       def __init__(self,email,password,name,address):
#             self.email = email 
#             self.password = password
#             self.name = name 
#             self.address = address

# user1 = User(email='test2@gmail.com',password = 'qwerty',name = 'nurbek',address = 'toktogula str 175 ')

# class order:
#       def __init__(self,user,items):
#             self.user=user 
#             self.items = items 

# order1 = order(user1,[{'product':product1,'quantity':1},{'product':product2,'quantity':3}])

# order1.user.address

# print(product1)
# print(product2)










# 1)
# class car:
#       def __init__(self, *args):
#             self.a = args 
#       def chr(self):
#             return self.a
# u = car('name=BMW','model=750','year=1998','country=German')
# print(u.chr())




