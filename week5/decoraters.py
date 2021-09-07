# def pizza_crust(i): # объявляем наш декоратор
#       return 'Tecто,сыр,соус,'+ i()
      
# def margarita():
#       return'томаты,базилик'

# @pizza_crust
# def margarita():
#       return'томаты,базилик'


# @pizza_crust
# def pepperoni():
#       return'колбаски'


# @pizza_crust
# def chili():
#       return'говяжий фарш,перец'

# print(margarita)
# print(pepperoni)
# print(chili)



# def hello_makers():
#       print('Hello,world!')
# print(type(hello_makers))


# Фунции это тоже объект 
# Функции относятся к объектам первого класса 

# Операции над объектами первого класса 
# 1) Можно хранить в переменных 

# def my_func():
#       print('Hello again')

# func1=my_func
# func1()

# OUTPUT: Hello again

# makers = hello_makers
# print(id(makers))
# print(id(hello_makers))

# OUTPUT: 
# 140692682284568
# 140692682284568

# У них одинаковые id потому что оба(makers,hello_makers) ссылаются на один объект 



#2)Функция может определять внутри себя другие функции

# Функция может принимать другую в качестве аргумента. 
# Функция может возвращать функцию в качестве результата 

# def func():
#       def func2():
#             a = 10
#       pass

# def func1(x):
#       pass 

# def func2():
#       pass

# class A:
#       pass 


# func1(10)
# func1('2')
# func1({})
# func1(func2)
# func1(A)





# def outer_func():
#       def inner_func():
#             print("can't stop addicting")
#       inner_func()

# outer_func()


# 3) Передавать функции в качестве аргумента 
# и возвращать их из других функций

# def main_func(func):
#       print(f'i got fucntion{func()}as argument')
#       func()
#       return func

# def hello_makers():
#       print('Hello,world!')

# print(main_func(hello_makers))


# def decorator(hgg): # 
#       def wrapper(*args): # 
#             print('first') #
#             print(hgg(*args)) #
#             print('last') #
#             return('finally') #
#       return wrapper #


# def hello(*args): #
#       args = str(args) #
#       return 'hello' + args #


# print(decorator(hello('world'))) #






# Декораторы это функции,для расширения возможностей других функций без изменения кода
# Декаратор должен принимать функцию, добавлять в нее функционал, и возвращать измененную функцию


# def decorator(function):
#       def wrapper(*args,**kwargs):
#             print('close your eyes')
#             res = function(*args,**kwargs)
#             print('and look deep in your soul')
#             return res
#       return wrapper

# @decorator
# def my_func1():
#       print('seasons in the abyss')

# @decorator
# def my_func2(x,y):
#       return x*y
# # print(my_func1())
# print(my_func2(20,10))

# decorator(my_func1)
# Записывает в файл, какая функция была вызвана,время, с какими аргументами. 






# 2) Создайте декоратор, который будет распечатывать дату и время вызова принимаемой функции, а затем вызывает саму функцию, например:
# @decorator
# def func():
#     print('Hello world')

# func() -> 
# Функция запущена 26.02.2021 21:51
# Hello World




# def decorator(func):
#       import datetime
#       def wrapper(*args,**kwargs):
#             current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#             func(*args,**kwargs)
#             with open('log.txt', 'a') as file:
#                   file.write(f'{func.__name__}\n')
#                   file.write(f'Функция запущена {current_time}\n')

#                   # моежете раскоментировать в случае чего
#                   # file.write(f'Args:{args}\n')
#                   # file.write(f'Kwargs:{kwargs}')
#                   # file.write('-----------------------\n')


#       return wrapper

# @decorator              
# def func1():
#       print('hello world')


# func1()




# Декаратор,замеряющий время выполнения функции(за n повторений)

# from tqdm import tqdm

# def timer(func):
#       import time
#       def wrapper(*args,**kwargs):
#             start = time.time()
#             func(*args,**kwargs)
#             end = time.time()
#             working_time = end - start
#             print(f'время выполнения функции{func.__name__}:{working_time} секунд')
#       return wrapper

# def timer(count=1):
#       import time
#       def decorater(func):
#             def wrapper(*args,**kwargs):
#                   total_time = 0
#                   for i in tqdm (range(count)):
#                         start = time.time()
#                         func(*args,**kwargs)
#                         end = time.time()
#                         working_time = end - start 
#                         total_time += working_time
#                   avg_time = total_time/count 
#                   print(f'время выполнения функции{func.__name__}:{avg_time} секунд')

#             return wrapper
#       return decorater

# @timer(count=20)       
# def func1():
#       print('hello')

# @timer
# def func2(x,y):
#       return x+y

# @timer(count=100) 
# def func3(url):
#       import urllib.request
#       urllib.request.urlopen(url)

# func3('https://www.aknet.kg/')


# func1()
# func2(20,19)
# func3()







# 5) Создайте словарь users и сохраните в нем несколько пользователей 
# (ключом будет имя пользователя, а значением пароль пользователя).
# Напишите следующую функцию:
# # def login(username, password):
# #     print(f'Welcome, {username}')
# Допишите к этой функции декоратор, который будет проверять есть ли в словаре пользователь с таким username и совпадает ли пароль.
# Если нет, то функция вызывает определенный тип исключения:


# users = {'Zhama':5, 'Tima': 8,'Ars':13}


# def decorator(func):
#       def wrapper(*args,**kwargs):
#             # try:

#             # except:
#             #       KeyError
                  

# def login(username, password):
#     print(f'Welcome, {username}')





# 4) Создайте декоратор, замеряющий время выполнения функции в секундах.
#  Затем объявите функцию, которая выполняет GET-запрос на 
#  главную страницу Google, оберните в декоратор и вызовите её


# from tqdm import tqdm

# def timer(func):
#       import time
#       def wrapper(*args,**kwargs):
#             start = time.time()
#             func(*args,**kwargs)
#             end = time.time()
#             working_time = end - start
#             print(f'время выполнения функции{func.__name__}:{working_time} секунд')
#       return wrapper

# def timer(count=1):
#       import time
#       def decorater(func):
#             def wrapper(*args,**kwargs):
#                   total_time = 0
#                   for i in tqdm (range(count)):
#                         start = time.time()
#                         func(*args,**kwargs)
#                         end = time.time()
#                         working_time = end - start 
#                         total_time += working_time
#                   avg_time = total_time/count 
#                   print(f'время выполнения функции{func.__name__}:{avg_time} секунд')

#             return wrapper
#       return decorater

# @timer(count=20)       
# def func1():
#       print('hello')

# @timer
# def func2(x,y):
#       return x+y

# @timer(count=20) 
# def func3(url):
#       import urllib.request
#       urllib.request.urlopen(url)

# func3('https://google.com/')


# func1()
# func2(20,19)
# func3()



# users = {'Zhama':5, 'Tima': 8,'Ars':13}


# def decorator(func):
#       def wrapper(*args,**kwargs):
#             # try:

#             # except:
#             #       KeyError
                  

# def login(username, password):
#     print(f'Welcome, {username}')













# Под вопросом ???????

# def func1():
#       print("i'm called inside other function ")

# def func2(func):
#       print("i'll do something before func calling")
#       func()

# def func3():
#       print('i hate niggers!!!!!!')

# func2(func3)



# Вложенные функции 

# def decorator (func):
#       print("new blood join this earth ")
#       def wrapper():
#             print("and quickly he's subdued")
#             print("Through constant pained disgrace")
#             func()
#             print("With time the child draws in")
#             return func
#       return wrapper

# @decorator
# def lyrics():
#       print("The young boy learns their rules")

# lyrics()





# def func(x):
#       return x*3
# func(10)
# func('2')
# func[1,2]





# 3) Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
# выделение жирным <b>...</b>\
# курсив <i>...</i>
# подчеркивание <u>...</u>.
# Далее создайте функцию которая будет возвращать текст “Hello world”, примените к этой функции цепочку декораторов


# def dec(func):
#       def wrapper(*args,**kwargs):
#             font_style


# def timer(func):
#       import time
#       def wrapper(*args,**kwargs):
#             start = time.time()
#             func(*args,**kwargs)
#             end = time.time()
#             working_time = end - start
#             print(f'время выполнения функции{func.__name__}:{working_time} секунд')
#       return wrapper


from functools import reduce
class ToDoList:
      def __init__(self):
            self.list_ = []
      def Put(self,to_do):
            self.list_.append(to_do)
      def get (self):
            print(self.list_)
            get = [[i.task, i.prio] for i in self.list_]
            print(get)
            if get: 
                  max_value = [reduce(lambda x,y: x if y > x else y,get)]
                  return max_value
            else:
                  return None

      def count(self,prio = 1):
            self.prio = prio 
            self.counts = []

            for i in self.list_:
                  if self.prio in range (1,6):
                        if i.prio == self.prio:
                              self.counts.append(i)
                              print(i)
            else: 
                  self.prio = 0 
            return f'{len(self.counts)}'


class Task(ToDoList):
      def __init__(self,task,prio=3 ):
            self.task = task 
            self.prio = prio
      def __str__(self):
            return f"{self.task} {self.prio}"


t = ToDoList()
a = Task('all these',5)
b = Task('things',3)
c = Task('fxdr',3)
t.Put(a)
t.Put(b)
print(t.get())
print(t.count(3))


# Напишите класс ToDoList для списка завершенных заданий. 

# Count выдает кол-во тасков в ToDoList, если параметр Priority, 
# должны быть посчитаны лишь Tasks, срочность кот-х соответсвует требуемости. 
# Как default argument вы можете взять 1; когда не лежит на интервале от 1 до 5, 
# выдайте 0
# И   спользуйте обычный Python-List внутренний тип данных ToDoList, 
# для GET используйте оператор <. Т.е Task меньше другого Task, 
# когда его срочность ниже. Используйте str, чтобы получить результат каждого таска, 
# а так же общий лист. 
# """




class Person:
  def info (self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name)
    print(self.age)

class Student(Person):
      def __init__(self, name, age, napr):
        super().__init__(name,age)
        self.napr = napr
      def display_student(self):
            print(f'{self.name} {self.napr}4 курс Политех, направление  IT ')

b1 = Student('Sanzhar', '19', 'VPI')
b2 = Student('Aibek', '19', 'IB')
# b1.display()
b1.display_student()
b2.display_student()






