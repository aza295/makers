#  ● 1  ФУНКЦИЯ - СОСТАВНАЯ КОНСТРУКЦИЯ КОТОРАЯ МОЖЕТ 
# ПРИНИМАТЬ ДАННЫЕ ВВОДА. ВЫПОЛНЯТЬ УКАЗАНИЯ И ВОЗВРАЩАТЬ ДАННЫЕ ВЫВОДА  



# ● ДЛЯ ЧЕГО ИСПОЛЬЗУЮТСЯ ФУНКЦИИ 
# 1) ДЛЯ ВЫЧИСЛЕНИЯ 
# 2) ДЛЯ ВЫПОЛНЕНИЯ ОПРЕДЕЛЕННЫХ ОПЕРАЦИЙ
# 3) НО ОСНОВНОЕ ПРЕИМУЩЕСТВО И ПЛЮС ФУНКЦИЙ ПРИ ИСПОЛЬЗОВАНИИ 
# ЭТО МНОГОКРАТНОЕ ИСПОЛЬЗОВАНИЕ КАКОГО ЛИБО КОДА
# ЧТО ОЧЕНЬ УПРОЩАЕТ РАБОТУ 

# ● ФУНКЦИИ В PYTHON МОГУТ ПРИНИМАЮТ  ПАРАМЕТРЫ ДВУХ 
# ТИПОВ ЭТО ОБЯЗАТЕЛЬНЫЙ И НЕ ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТРЫ

 

# СИНТАКСИС ФУНКЦИЙ 

# def имя_функции[параметры]
#       определение функции 

# ИМЯ ФУНКЦИИ ЗАДАЕТСЯ ТАК ЖЕ КАК И ИМЕНА ПЕРЕМЕННЫХ 




# def hello():
#     print('Hello world')
#     return ('dgsd')
# (hello)
# hello()
# hello()

# OUTPUT:
# Hello world
# Hello world
# Hello world


# x = int(input('Enter first number:'))
# z = int(input('Enter second number:'))

# def sum (a,b):
#       return a + b 
# print(sum(x,z))


# ●  SECOND WAY TO MAKE IT EASIER 

# x = int(input('Enter first number:'))
# z = int(input('Enter second number:'))

# def sum (a,b):
#       return a + b 

# z - sum(x,z)    
# print(sum(z)









# def f (a=8):
#       return 2*a -2

# print(f())
# OUTPUT: 14

# ЕСЛИ МЫ НИЧЕГО НЕ УКАЗЫВАЕМ В PRINT БУДЕТ 
# ВЫВОДИТЬ НЕОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР
# НО ЕСЛИ УКАЗАТЬ В PRINT ПАРАМЕТР 8 ОТБРОСИТ ТАК КАК 
# ЭТО НЕОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР 




# 8 ЭТО НЕ ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР НО ВВЕДЕННЫЕ ДАННЫЕ В PRINT 
# БУДУТ ГОРАЗДО ПРИОРИТЕТНЕЕ

# def f (a =8, *args):
#       return 2*a -2

# print(f(a=10, 2,3,44,5,6,6,77))

# OUTPUT: 18




# 8 ЭТО НЕ ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР НО ВВЕДЕННЫЕ ДАННЫЕ В PRINT 
# БУДУТ ГОРАЗДО ПРИОРИТЕТНЕЕ






# ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕННЫХ 

# a = 24
# b = 24
# def f(a):
#       a = 24
#       b = 24
#       print(a)
#       print(b)
# print(a)
# print(b)


# def substruct():
#     num1 = 20
#     num2 = 5
#     print('num1+num2')
#     return num1- num2
# substruct()
    

# variable = substruct()
# print(variable)



# list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,substruct()]
# print(list_)

# def substruct():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return (num1 - num2)
# substruct()
    
# def function():
#       print("I'm calling substruct function")
#       substruct()
# print(function())


# def divide(a,b):
#       return a / b
# num1 = 70
# num2 = 10
# num3 = 2
# print(divide(num1,num2))
# print(num1)
# print(num2)

# def welcome(name,last_name):
#       return f'Welcome,{name}{last_name}'
# name = input()
# last_name= input()
# print(welcome(name,last_name))


# CLASS WORK 


# a1= 100
# a2= 200
# a3= 300
# a4= 400
# a5= 500

# #ОБЪЯВЛЕНИЕ ФУНКЦИИ 
# def count(num):
#       return (num**2)/15*10
# # ВЫЗОВ ФУНКЦИИ
# count(a1)
# count(a2)
# count(a3)
# count(a4)
# count(a5)

# print(count (a2))

# a! = 1*2*3*4*5*6*7*8*9*10

# a1= 5
# fact = 1 
# for i in range (1, a1 +1): 
#       fact *= i
# a2= 6
# a3= 8
# a4= 7
# a5= 11


# a1 = 5
# a2 = 10
# a3 = 15
# a4 = 20
# a5 = 25
#  под вопросом 

# def factorial(num):
#     fact = 1
#     for i in range (1, num +1): 
#         fact *= i
#     return fact 

# fact1 = factorial(a1)
# print(fact1)
# fact2 = factorial(a2)
# fact3 = factorial(a3)
# fact4 = factorial(a4)
# fact5 = factorial(a5)

# АННОТАЦИЯ ТИПОВ
# ПОД ВОПРОСОМ 
# def summarize (x:int,y:int) -> int:

#      '''ПРИНИМАЕТ 2 ЧИСЛА И СКЛАДЫВАЕТ МЕЖДУ СОБОЙ'''  #docstring
#     return x + y 

# summarize(2,5)
# summarize('2','5')
# summarize([1,2,3][4,5,6])
# summarize((1,2,3),(4,5,6))




# a1 = 20

# a1 ** 2 - a1 ** 3
# pow(a1,2) - pow (a2,3)

# a1 = 5
# a ** 2 - a1 * 10

# import operator 
# a1 = 5 
# a1 ** 2 - a1 *10 


# operator.pow (a1,2) - operator.mul(a1,10)

# def func (a,b,c):
#       return (a,b) * c   
# func (1,2,3,) #9
# func('1','2',5 )
# func([1],[2],5) 



# ПАРАМЕТРЫ ЭТО ЗНАЧЕНИЯ ФУНКЦИИ ПРИ ОБЪЯВЛЕНИИ 

# АРГУМЕНТЫ ЭТО ЗНАЧЕНИЯ ДЛЯ ПАРАМЕТОРОВ ПРИ ВЫЗОВЕ 


# ПАРАМЕТРЫ БЫВАЮТ 2 ТИПОВ ОБЯЗАТЕЛЬНЫЕ И НЕОБЯЗАТЕЛЬНЫЕ (ПО УМОЛЧАНИЮ)

# from os import error


# def func (a,b=1):
#       return a+b 

# print(func(10))

# func(10) OUTPUT 11
# func(10,2) OUTPUT 12
# func(10,2,5)error






# def func (a,b, c = 0):
#       return a + b + c

# #ПОЗИЦИОННЫЕ АРГУМЕНТЫ 
# func (10,12)#22
# func (10,12,24)

# ИМЕНОВАННЫЕ 
# func (a=5,b=6)#11
# func (a=6,b=8,c=10) #24
# func(b=10,c=9,a=5)


# ПОЗИЦИОННЫЕ АРГУЕМЕНТЫ УКАЗЫВАЮТСЯ В ТОЙ ПОЗИЦИИ 



# ИМЕННОВАННЫЕ АРГУМЕНТЫ ВСЕГДА ДОЛЖНЫ СЛЕДОВАТЬ ЗА ПОЗИЦИОННЫМИ 















# f(x) = 2*x -2
# у нас есть фунция  f от x равняется 2 умноженное на -2

# В ЯЗЫКЕ PYTHON









# a = str(input('Enter your name:'))

# def i(aa):
#       return len(aa)

# print(i(a))

# def hello(a):
# #     print('Hello world')
#       a = "ghjggh"
#       return a
# print(hello(1))





# def notify_users(users:list):
#       pass  
# notify_users([test1@gmail.com,test2@gmail.com])

# notify_users([user1,user2])



# def notify_users(*users):
#       pass

# notify_users(user1,user2)


# args (МНОЖЕСТВО ПОЗИЦИОННЫХ АРУГЕМЕНТОВ)

# kwargs (МНОЖЕСТВО ИМЕННОВАННЫХ АРГУМЕНТОВ)



# def func(a,b,c d =0,e=2, *args,**kwargs)
#     pass

# func(1,2,3,4,5)
# func(1,2,3,4,5)
# *args -> (6,7)
# **kwargs -> {'f':10,'g': 23}



# def my_func(a,b,c):
#       return a+b+c

# my_func(1,2,3)
# my_func(a=1,b=2,c=3)

# list1 =[2,3,4]
# my_func(*list1)
# my_func(*tuple1)

# dict1 = {'a':1,'b':2,'c':3}
# my_func (**dict1)
# my_func(a=1,b=2,c=3)





# def my_func(a,b,c):
#       return a+b+c

# my_func(1,2,3)
# my_func(a=1,b=2,c=3)

# list1 =[2,3,4]
# my_func(*list1)
# my_func(*tuple1)

# dict1 = {'a':1,'b':2,'c':3}
# my_func (**dict1)
# my_func(a=1,b=2,c=3)

# 6) Создайте функцию, которая принимает и выводит \
# "It's odd number" если это число не кратно двум и "It's even number" в противном случае.

# a = 27
# b = 35
# c = 40

# def max_value(a,b,c):
    
#     if a>b and a>c:
#         print('max_value=',a)
#     elif b>a and b>c:
#         print ('max_value=',b)
#     elif a==b:
#         print("a=b") 
#     elif a==c: 
#          print("a=c")
#     elif b==c:
#         print("b=c")
#     else:
#         print(c)
#     return(max(a,b,c)) 
# print(max_value(a,b,c))


# a = (input('Enter anything'))
# b = (input('Enter annything'))
# def max_value(a,b):
#     return(type(a,b,max_value))
# print(max_value(a,b))
# def type_of (z, x):
#     return type(z), type(x)
# print (type(z),(x))


# 3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# """

# # def f (a =8,b=27,c=15):
# #       return max()

# # print(f(a=10)


# def is function, multiply is name of function 
# name can be anything

# def multiply(a):#a это временная переменная 
#     b = 1 # b = 1 это 
#     for i in a:
#         print(b)
#         b*=i
#     return b
# list_ = [15,20,3,4]

# print(multiply(list_))

# OUTPUT:24

# def multiply(a):#a это временная переменная 
#     b = 0 # b = 1 это 
#     for i in a:
#         # b = 0 +15   КОЛИЧЕСТВО ИТЕРАЦИЙ
#         # b = 15 + 20
#         # b = 35 + 3 
#         # b = 38+ 4
#         # b= 42
#         # b = b + i
#         b += i
#     return b
# list_ = [15,20,3,4]

# print(multiply(list_))

# OUTPUT:24



