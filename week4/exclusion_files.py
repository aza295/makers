# ● B  python ЕСТЬ ВСТРОЕННЫЕ СРЕДСТВА ДЛЯ РАБОТЫ С ФАЙЛАМИ: ОТКРЫТИЕ,ЗАКРЫТИЕ,ЧТЕНИЕ И ЗАПИСЬ

# СУЩЕСТВУЕТ 3 РЕЖИМА РАБОТЫ С ФАЙЛАМИ
# ● 1) "r" режим чтения 
# ● 2) "w" режим записи
# ● 3) "a" режим добавления 
# ● 4) "x" запись в новый файл

# ФАЙЛЫ БЫВАЮТ ДВУХ ТИПОВ, ТЕКСТОВЫЕ И БИНАРНЫЕ.  



# 1) ШАГ ПРИ РАБОТЕ С ФАЙЛАМИ ЭТО ОТКРЫТИЕ САМОГО ФАЙЛА 
# ДЛЯ ЭТОГО ИСПОЛЬЗУЕТСЯ ФУНКЦИЯ  open
# ОБЫЧНО В ЭТУ ФУНКЦИЮ ПЕРЕДАЮТ ДВА АРГУМЕНТА 
# 1) ЭТО ИМЯ ФАЙЛА  
# 2) РЕЖИМ В КОТОРОМ ОТКРЫВАЕТСЯ ФАЙЛ 

# ЕСЛИ ПРИ ВЫЗОВЕ open() ВТОРОЙ АРГУМЕНТ НЕ УКАЗАН, ТО ФАЙЛ ОТКРЫВАЕТСЯ В РЕЖИМЕ ЧТЕНИЯ ('r')
# ФУНКЦИЯ  open ВОЗВРАЩАЕТ ОБЪЕКТ ФАЙЛОВОГО ТИПА 


# f = open('love_message.txt','r')
# print(f.read())
# f.close()


# with open('love_message.txt','a') as y:
#       y.write( ' A love message to the world')


# КАК ОТКРЫТЬ ФАЙЛ НАХОДЯЩИЙСЯ В ДРУГОЙ ДИРЕКТОРИИ

# 1) ПРОПИСЫВАЕМ ПУТЬ ДО ЭТОЙ ДИРЕКТОРИИ ГДЕ НАХОДИТЬСЯ НАШ ФАЙЛ
# 2) ПЕРВЫМ АРГУМЕНТОМ ПЕРЕДАЕМ (task1.txt) ИМЯ ФАЙЛА 
# 3) ВТОРЫМ АРГУМЕНТОМ ПЕРЕДАЕМ  РЕЖИМ В КОТОРОМ ОТКРЫВАЕТСЯ ФАЙЛ (read)

# СЕЙЧАС МЫ НАХОДИМСЯ В ДИРЕКТОРИИ week5 В КОТОРОМ ХРАНИТСЯ ФАЙЛ task2.txt

# ПРИ ПОПЫТКЕ ОТКРЫТЬ ФАЙЛ task1.txt ВЫХОДИТ ОШИБКА ТАК КАК 

# python НЕ ВИДИТ ФАЙЛ task1.txt ОН НАХОДИТСЯ В WEEK4 

# КАК ОТКРЫТЬ ФАЙЛ НАХОДЯЩИЙСЯ В ДРУГОЙ ДИРЕКТОРИИ 

# ПИШЕМ task = open('/home/aziz/Desktop/makers/week4/task1.txt','r')

# task = open('/home/aziz/Desktop/makers/week4/task1.txt','r')


# OUTPUT: fggffgfg



# ● 1) with w(write) we only can open and write something in the file, can't read 

# but we can  
# write and read 
# with this:
# w+ write + read 

#  with fucntion w(write) we wrote  'work hard' 

# file0 = open('bootcamp.txt','w')
# print(file0.write('work hard '))

# ● " w" УДАЛЯЕТ СОДЕРЖИМОЕ И ПОВЕРХ ЗАПИСЫВАЕТ НОВОЕ 
# write(str) ЗАПИСЫВАЕТ ПО ОДНОЙ СТРОКЕ 

# write()

# ● "х" НЕ ЗАПИСЫВАЕТ В СУЩЕСТВУЩИЙ ФАЙЛ 

# ● "a" ДОЗАПИСЫВАЕТ НЕ УДАЛЯЯ ПРЕЖНИЙ ФАЙЛ




# ● 2) with r(read) we only can read the file, can't change or add something

# ЕСЛИ МЫ ИСПОЛЬЗУЕМ write ТО ОН УДАЛЯЕТ СУЩЕСТВУЮЩИЕ ФАЙЛЫ ВНУТРИ ФАЙЛА.txt

# after we use read to read what's inside bootcamp.txt

# we also can do this 
# r+ - read =write 

# file0 = open('bootcamp.txt','r')
# print(file0.read())

# OUTPUT: work hard 

# ● МЕТОД read СЧИТЫВАЕТ СОДЕРЖИМОЕ ВСЕГО ФАЙЛА В ВИДЕ ОДНОЙ БОЛЬШОЙ СТРОКИ 

# ● МЕТОД readlines СЧИТЫВАЕТ ВСЕ СОДЕРЖИМОЕ ФАЙЛА В ВИДЕ СПИСКА ИЗ СТРОК

# ● МЕТОД readline СЧИТЫВАЕТ КАЖДЫЙ РАЗ ПО ОДНОЙ СТРОКЕ 







# ● 3) МЕТОД (а)append В ОТЛИЧИИ ОТ w(write) ДОБАВЛЯЕТ НОВЫЕ ФАЙЛЫ НЕ УДАЛЯЯ СУЩЕСТВУЮЩИЕ ФАЙЛЫ
# def m_func1(a):
#       return if str(a)[::-1]
# print(m_func1(-356))

# file0 = open('bootcamp.txt','a')
# print(file0.append('Twisting your mind and smashing your dreams'))

# OUTPUT:  


# JSON( JavaScript Object Notation)


# human = {'name':'Claus',
#       'surname':'Meine',
#       'occupation':'singer',
#       'country':'German',
#       'is_married':False,
#       'driving_license':None,
#       }

# import json

# json_str = json.dumps(human)
# print(json_str)


# people_json= '[{"name":"Vadim","last_name":"rebrov","curator":"alex"},{"name":"max","last_name":"zeevnov","curator":"null"}]'
# people = json.loads(people_json)
# print(people)


# dumps(python_obj)-переводит python объект в json  строку 

# loads()-переводит json строку  в python объект

# human = {"name":"Claus",
#       "surname":"Meine",
#       "occupation":"singer",
#       "country":"German",
#       "is_married": false,
#       "driving_license":null,
#       }






# task = open('/home/aziz/Desktop/makers/week4/task1.txt','a')
# print(task.write("\tNo one like you"'\n'
# "I can't wait for the nights with you"'\n'))







# dump ()запись python объектов в json файл 

# product =[
#       {
#       'title':'Samsung s21',
#       'price':65000
#       },
#       {
#       'title':'xiaomi mi 11',
#       'price':50000

#       },
#       {
#       'title':'iphone 12',
#       'price':80000
#       }

# ]
# import json 
# f = open('products.json','w')
# json.dump(product,f)
# f.close()



# #  laod чтение объектов из json файла

# f = open('products.json','r')
# content = f.read ()
# product= json.loads(content)

# f = open('products.json','r')
# product = json.load


# В json: 
# ключом может быть только строка 
# кавычки всегда должны быть двойными  


# import json
# company ={'name':'McDonald\'s','adress':'Washington'}
# res= json.dumps(company)
# print(res)


# Python                              JS  
# int,float                           number  
# str                                 string
# list,tuple                          array
# dict                                object   
# True/False                          true/False 
# None                                null  



# Фио, Дата рождения,Адрес 
# from functools import reduce


1, 




# tell() сообщает текущую позицию 



# import csv 

#ЗАПИСЬ 


# with open ('students.csv','w') as f:
#       stud_writer = csv.writer(f)
#       stud_writer.writerow(['#','ФИО','дата рождения','адрес'])
#       stud_writer.writerow(['1','What the fuck','is','this','03.08.2021', 'street logvinenko 12'])


#ЧТЕНИЕ 
# import csv 
# with open ('students.csv','r') as file:
#       csv_reader = csv.reader(file,delimiter=',')
#       for row in csv_reader:
#             print(row)

# import csv 
# with open ('students.csv','r') as file:
#       csv_reader = csv.reader(file,delimiter=',')
#       for row in csv_reader:
#             print(row)


# with open ('students.csv','w') as file:
#       csv_writer = csv.DictWriter(file,['#'
#       ,'ФИО','дата рождения','адрес'])
#       csv_writer.writeheader()
#       csv_writer.writerow({'#':1,
#       'ФИО':'september eleven','дата рождения':'11.09.2001','адрес':'twin towers'})

# with open ('students.csv','r') as file:
#       print(file.read())





# 1) Создайте файл text.txt, 
# в него запишите числа от 1 до 10, 
# каждое из которых на новой строке. 
# Затем откройте его и распеча1
# тайте только четные числа.

# with open ('test.txt','') as o:
#       for i in o:
#             if (i)%2==0:
#                   print(i)


# OUTPUT: 
2
4
6
8
10


# 2) Откройте файл task2.txt в режиме записи.
#  Запишите в него 10 любых чисел, каждое из которых будет
#  на новой строке.

# with open ('test.txt','w') as o:
#       print(o.writelines('1,2,6,7,8,9,10'))





# 3) Дан список состоящий из строк. Переведите каждый 
# элемент этого списка в целочисленное значение используя 
# встроенную функцию, решите это задание тремя способами.

#number 1
# a=['1','3','5','7','10']
# b = list(map(int,a)
# print(b)

# a=['1','3','5','7','10'] # создаем список 
# def v(a):   # создаем функцию которая хранит в себе данные переменной a 
#       return int(a)  #вернуть целочисленное значение a так как a у нас строки 
# z = list(map(v,a)) # 
# print(z)



# b= list(map(lambda x: int))







# 4) Запросите у пользователя ввод числа n значением от 1 до 10(обработав возможную ошибку).
#  Затем пройдитесь по промежутку чисел от 1 до 100 и запишите в словарь только те числа, которые кратны n.
#  Ключом будет само число, а значением его квадрат. Используйте comprehensions






# try: 
#       a = int(input('enter any number:'))
#       b =  {i: i**2 for i in range(1,101) if i %a==0 }
#       print(b)
# except ValueError:
#       print('wrong')
# except NameError:
#       print('wrong again')






# 7. Создайте переменную list_ и сохраните в нем список из чисел. Выведите произведение всех этих чисел. Результат сохраните в новой переменной new_list и выведите в консоль. Используйте встроенную функцию.


# from functools import reduce 
# list_ = [19,27,30]
# list2 = reduce(lambda x,y:x+y,list_)
# print(list2)

# 10. Создайте переменную list_ и сохраните в нем список со строками. 
# Найдите самое длинное имя из списка функцией reduce.
# Результат сохраните в новой переменной new_list и выведите в консоль. Используйте встроенную функцию.
# from functools import reduce 
# list_ = ['wood','prick','break','prayer']
# new_list = reduce(lambda x,y: x if len(x)>len(y) else y ,list_) 
# print(new_list)



# 8. Создайте переменную list_ и сохраните в нем список из чисел. 
# Посчитате количество чётных и нечётных чисел в этом списке. 
# Результат сохраните в новой переменной new_list и выведите в консоль. Используйте встроенную функцию.
# Пример:
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
# Output: even: 5, odd: 5


# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = list(filter(lambda x: x%2==0,list_)) 
# even = list(filter(lambda x: x%2!=0,list_))
# print(f'{len(odd)} odd numbers,{len(even)} even numbers')






#4 Создайте переменную list_ и сохраните в нем список из чисел. 
# Создайте новый список, состоящий из квадратов этих чисел, 
# результат сохраните в новой переменной new_list и выведите в консоль. Используйте встроенную функцию.

# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = list(map(lambda x: x**2,list_))
# print(list2)




# 7. Вам дан список из нескольких имён в нижнем регистре.
#  Напишите функцию nameList которая принимает данный список и возвращает новый 
# список где первая буква имени в верхнем регистре.
# Пример:
# input: ['pipi', 'papa', 'mama']
# output: ['Pipi', 'Papa', 'Mama']

# def namelist (a):
#       return [x.title() for x in a]
# b = ['pipi', 'papa', 'mama']
# c = []
# print(namelist(b))









# 8. Напишите функцию count_symbols, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы.
# Пример:
# input: "Мурат супер"
# output: Количество гласных: 4, Количество согласных: 6, Количество остальных символов: 1




# a=[]
# print(i for i in range (1,11))

# def getListNum ():
#       for i in range(11):
#             c.append(i)
# c = []
# getListNum()
# print(c)

# print(i for i in range(11))



# newlist = [x for x in range(11)]
# print(newlist)


#9. Откройте файл task3.txt в режиме записи. 
# Запишите в него 10 любых чисел в столбик. 
# Затем вернитесь в начало файла и распечатайте записанные числа.


# with open('task3.txt','w') as o:
#       for i in range(11):
#             print(i)




# Вам предоставляются два непустых связанных списка,
#  представляющих два неотрицательных целых числа. 
# Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру. 
# Добавьте два числа и верните сумму в виде связанного списка.

# Вы можете предположить, что эти два числа не содержат никакого начального нуля, кроме самого числа 0.

# l1 =[2,4,3] # создаем список 
# l2 = [5,6,4] # создаем второй список 
# def t (ss): # создаем функцию 
#       a = '' # создаем пустую строку 
#       print(a) #  
#       for i in ss[::-1]: #
#             a += str(i) #
#       return a # 
# l1 = t(l1) # 
# l2 = t(l2) #
# l3 = int(l1) + int(l2) #
# print (l3) #


# l3 = 807
# def v (zz):
#       a = []
#       print(a)
#       for i in zz[::-1]:
#             return i
# print (l3)







# print(l1)
# print(l2)

# l1 = [2,4,3];l2 = [5,6,4]
# b = filter(reversed(l x:x+x,l1))
# print(b)




# """
# 1) Создайте функцию, которая будет принимать 2 числа, 
# далее программа должа выполнять операции "+ - * /" в зависимости от выбора пользователя
# """

# def mmm ():
#       x = input ("what we will do ?(+,-):")
#       a = int(input('enter number:'))
#       b = int(input('enter second number:'))
#       if x == "+":
#           print (a + b)
#       elif x == '-':
#           print (a - b)
# print(mmm())

            
# 2) Откройте файл task.txt. В нём в нескольких строках записан текст. 
# Прочтите содержимое и распечатайте количество непустых строк.


# with open ('task3.txt','r') as o:
#       b = 0
#       for i in o:
#             if i != '\n':
#                   b+=1
# print(b)





# 3. Откройте файл task2.txt. В нём в нескольких строках записан текст.
#  Прочтите содержимое и распечатайте только числа.

# with open ('task3.txt','r') as a:
#       for i in a.read():
#             if i.isdigit():
#                   print(i)


      


# 4) Дан список состоящий из чисел. 
# Пройдитесь по спику, четные числа возведите в квадрат, 
# а нечетный в куб решите это задание используя встроенную функци


a = [2,5,6,7,10] # создаем список 

def f(a): # вызываем функцию
      if a %2 ==0: #
            return a **2 #
      else: 
            return a **3 #
b = list(map(f,a)) # 
print(b) #
# f(a)


# 5) Создайте словарь, где ключами будут строки,а значениями числа. 
# Пройдитесь по элементам, если значение элемента > 5 запишите вместо числа строку 'more', 
# если меньше то 'less'. (Используйте comprehensions)


# a = {'1':4,'3':5,'5':7} # создаем список 
# b = {k:'more' if v >5  # пишем ключ k:'more' more уже записывается как значение и если значение больше 5 оно 
# поменяет его на more  if v >5
#      else 'less' 
# иначе на less
#      for k,v in a.items() 
#      }
# print(b)



