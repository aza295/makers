# ТИПЫ ДАННЫХ СПИСКИ

# ● СПИСОК В python это встроенный тип данных
# представляющий собой одну из разновидностей структур данных

# ● СПИСКИ - ЭТО ОДНА ИЗ СТРУКТУР
# ДАННЫХ ИСПОЛЬЗУЮТСЯ ОНИ ДЛЯ ХРАНЕНИЯ И РАБОТЫ С КАКОЙ ЛИБО 
# ИНФОРМАЦИЕЙ

# ● Список (list) представляет тип данных, который хранит 
# набор или последовательность элементов.
#  Для создания списка в квадратных скобках ([]) через запятую
#   перечисляются все его элементы. 
#   Во многих языках программирования есть аналогичная структура данных, 
#   которая называется массив. 
#   Например, определим список чисел:

# ●  Также для создания списка можно использовать конструктор list(): 

# ● numbers1 = [] 
# ● numbers2 = list() 


# ●  list списки 

# numbers = [3,4,5,9,12]
# print (numbers)
# output [3, 4, 5, 9, 12]


# ● list списки

# numbers = [3,4,5,35.1,'string']
# print (numbers)
# output [3, 4, 5, 35.1, 'string']

# ● ДОБАВЛЕНИЕ СПИСКА ВНУТРИ СПИСКА 

# numbers = [33,5,33.1, [45.7]]
# print (numbers)
# OUTPUT [33, 5, 33.1, [45.7]]

# ● ДЛЯ ТОГО ЧТОБЫ  ОБРАТИТЬСЯ К ОПРЕДЕЛЕННОМУ ЭЛЕМЕНТУ В СПИСКЕ 
# МЫ ДОЛЖНЫ УКАЗАТЬ ИМЯ СПИСКА И В [] ЕГО ПОРЯДКОВЫЙ НОМЕР ИЛИ 
# ИНАЧЕ ЭТО НАЗЫВАЕТСЯ INDEX

# names = ['water','ice', 'tea','freeze', 'cold','hot','red','hot','chili','peppers']
# print (names[7])
# OUTPUT hot

#  ● ЦИКЛ FOR, ЦИКЛ СО СЧЕТЧИКОМ FOR РАБОТАЕТ С ИТЕРИРУЕМЫМИ 
#  ОБЬЕКАТАМИ 
#  СПИСКИ ЭТО ВСЕГДА ИТЕРИРУЕМЫЕ ОБЬЕКТЫ

# stings = ['water','ice', 'tea']
# for sting in stings:
#       print (stings)
# OUTPUT names = ['water','ice', 'tea'

#  ● ЦИКЛ FOR

# stings = ['water','ice', 'tea']
# for sting in stings:
#       print (stings)
# OUTPUT  ['water', 'ice', 'tea']
# ['water', 'ice', 'tea']
# ['water', 'ice', 'tea']


# ● append  ДОБАВЛЯЕТ СТРОКУ В КОНЕЦ СПИСКА

# strokes = ['red','hot','chili','peppers']
# strokes.append('one of my favorite bands')
# print (strokes)

# OUTPUT ['red', 'hot', 'chili', 'peppers', 'one of my favorite bands'
# .append ДОБАВЛЯЕТ СТРОКУ В КОНЕЦ СПИСКА

# ● МЕТОД .pop()
# pop([index]): удаляет и возвращает элемент по индексу index. 
# Если индекс не передан, то просто удаляет последний элемент.

# cwb = ['lost', 'aware','error']
# cwb.pop()
# print (cwb)
# output ['lost', 'aware']



# ● МЕТОД index 
# Функция Index - это встроенный метод списка, который позволяет 
# узнать индекс или позицию элемента в последовательности.

# Другими словами, этот метод ищет элемент в списке и возвращает 
# его индекс.

#  ●
# names = ['water','ice', 'tea','freeze', 'cold']
# n=names.index('freeze')
# print (n)
#output 3


# print (type(numbers))
# otput list


# ● МЕТОД СОРТРОВКИ - СОРТИРУЮТ СПИСОК ПО ВОЗРАСТАНИЮ


# mk = [8,3,15,47,68,99,144]
# mk.sort()
# print(mk)

# OUTPUT [3, 8, 15, 47, 68, 99, 144]


# ● МЕТОД СОРТИРОВКИ REVERSE СОРТИРУЕТ ЧИСЛА 
# ПО УБЫВАНИЮ


# mk = [11,9,1,44,19,81,144]
# mk.sort(reverse = True)
# print(mk)

# OUTPUT [144, 81, 44, 19, 11, 9, 1] 

# ● ИЗМЕНЕНИЕ ЭЛЕМЕНТА СПИСКА
# mk = [8,3,15,47,68,99,144]
# mk [1]= 'c' #УКАЗЫВАЕТСЯ INDEX ПОЭТОМУ ЗАПИСАЛ 1
# print(mk)
# OUTPUT [8, 'c', 15, 47, 68, 99, 144]

# ● СОРТИРОВКА СТРОК И ЧИСЕЛ ВЫДАЕТ ОШИБКУ  

# mk = [8,3,15,47,68,99,144]
# mk [1]= 'c'
# mk.sort()  # OUTPUT TypeError: not supported between instances of 'str' and 'int'
# print(mk)


# ● Кроме того, если нам необходим последовательный список чисел, то для его создания удобно использовать функцию range, которая имеет три формы:

# ● range(end): создается набор чисел от 0 до числа end 

# ● range(start, end): создается набор чисел от числа start до числа end 

# ● range(start, end, step): создается набор чисел от числа start до числа end с шагом step 



# numbers = list(range(10)) 
# print(numbers)

# ● IF ELIF ELSE STRUCTURE

# age = 26
# if (age >= 25 ):
#       print ('you can enter alone ')
# elif (age >18 and age < 25):
#       print ('you can enter with adults')
# else: 
#       print ("you can't enter")


# ● ФУНКЦИЯ ЭТО СОСТАВНАЯ КОНСТРУКЦИЯ 
# КОТОРАЯ МОЖЕТ ПРИНИМАТЬ ДАННЫЕ ВВОДА.
# ВЫПОЛНЯТЬ УКАЗАНИЯ И ВОЗВРАЩАТЬ ДАННЫЕ ВЫВОДА

# ● ФУНКЦИИ ИСПОЛЬЗУЮТСЯ ДЛЯ ВЫЧИСЛЕНИЯ 
# ДЛЯ ВЫПОЛНЕНИЯ ОПРЕДЕЛЕННЫХ ОПЕРАЦИЙ 
# НО ОДНА ИЗ ГЛАВНЫХ ОСОБЕННОСТЕЙ И ПЛЮСОВ ИСПОЛЬЗОВАНИЯ ФУНКЦИЙ 
# ЭТО МНОГОКРАТНОЕ ИСПОЛЬЗОВАНИЕ КОДА ЧТО ОЧЕНЬ УПРОЩАЕТ РАБОТУ 

#  ● ОПРЕДЕЛЕНИЕ ФУНКЦИЙ 

#  DEF ИМЯ_ФУНКЦИИ (ПАРАМЕТРЫ):
#       ОПРЕДЕЛЕНИЕ ФУНКЦИИ

# def string():
#       print('rock you like hurricane')
# string()
# OUTPUT: rock you like hurricane

# ● МНОГОКРАТНОЕ ИСПОЛЬЗОВАНИЕ ФУНКЦИЙ

# def string():
#       print('rock you like hurricane')
# string()
# string()
# string()
# string()
# # OUTPUT:
# rock you like hurricane
# rock you like hurricane
# rock you like hurricane
# rock you like hurricane


# ● ОПЕРАЦИЯ ВЫЧИСЛЕНИЯ И РАБОТА С ДАННЫМИ

# x = int(input("enter first number:"))
# y = int(input("enter second number:"))

# def sum (a,b):
#       return a + b 
# print (sum (x,y))

# ● ANOTHER VERSION OF DO THIS 

# x = int(input("enter first number:"))
# y = int(input("enter second number:"))

# def sum (a,b):
#       return a + b 
# z = sum(x,y)
# print (z)

# ● insert добавляет элемент item в список по индексу index

# strokes = ['eddie', 'halen']
# strokes.insert(1,'van')
# print (strokes)

# OUTPUT  ['eddie', 'van', 'halen'

# ● index(item): возвращает индекс элемента item. 
# Если элемент не найден, генерирует исключение 
# ValueError 

# oc = ['windows','mac','linux']
# oc.index('mac')
# print (oc.index('linux'))

# OUTPUT: 2 


# ● ФУНКЦИЯ REMOVE 

# languages = ['JavaScript','Python','Pascal','Frontend']

# for item in languages:
#       if item ==  'Frontend':
#             languages.remove(item)
# print (languages)

# OUTPUT 
# ['JavaScript', 'Python', 'Pascal']


# ● count(item): возвращает количество вхождений 
# элемента item в список 

# css = ['tea','water','tea','coffee']
# print (css.count('water'))
# OUTPUT 1 

# css = ['tea','water','tea','coffee']
# print (css.count('tea'))
# OUTPUT 2


# ● min(cpsu): возвращает наименьший элемент списка 

# cpsu = [26,25,35,45,65,75,85,95]
# print (min(cpsu))
# OUTPUT 25



# cpsu = [15,25,35,45,65,75,85,95]
# print (min(cpsu))

# OUTPUT 15


# ● max(list): возвращает наибольший элемент списка

# digits = [100,200,300,400,500]
# print (max(digits))
# OUTPUT 500



# ●  Кроме метода sort мы можем использовать встроенную функцию 
# sorted, которая имеет две формы: 

# ● sorted(list): сортирует список list 

# ● sorted(list, key): сортирует список list, 
# применяя к элементам функцию key 

# names = ['Stewie','Stan Smith','Peter Griffin']
# print (sorted(names))
 
# OUTPUT ['Peter Griffin', 'Stan Smith', 'Stewie']



# ●  Копирование списков 
# Это так называемое "поверхностное копирование"
# И чтобы происходило копирование элементов, 
# но при этом переменные указывали на разные списки, 
# необходимо выполнить глубокое копирование (deep copy).

# bands1 = ['Metallica','Megadeth','Slayer']
# bands2 = bands1
# bands2.append ('Anthrax')
# print (bands1)
# print (bands2)

# OUTPUT 
# ['Metallica', 'Megadeth', 'Slayer', 'Anthrax']
# ['Metallica', 'Megadeth', 'Slayer', 'Anthrax']

# ●  deepcopy()
# ВОПРОС ОСТАЕТСЯ ОТКРЫТЫМ 

# abcd = ('beer','vodka','tequila')
# abcd2 = copy.deepcopy(favorites)
# abcd2.append ('all alcho drinks')
# print(abcd)
# print(abcd2)

# ФУНКЦИЯ RANGE 

# ● RANGE(END): создается набор чисел от 0 до числа end 

# numbers = list(range(11))
# print (numbers)
# OUTPUT [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ● RANGE(START,END): создается набор чисел от числа start до числа end 

# digits = list(range(25,36))
# print (digits)
# OUTPUT  [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# ● RANGE(START,END,STEP): создается набор чисел 
# от числа start до числа end с шагом step 


# ccc = list(range(1,13,2))
# print (ccc)
# OUTPUT [1, 3, 5, 7, 9, 11]


# ● RANGE(START,END,STEP) СПИСОК В ОБРАТНОМ ПОРЯДКЕ 

# acdc = list(range(13,1,-2))
# print (acdc)
# OUTPUT [13, 11, 9, 7, 5, 3]


# ● FOR + RANGE
# ● RANGE + ВОЗВЕДЕНИЕ В СТЕПЕНЬ

# for cd in range (1,11):
#       print(cd**3)

# OUTPUT
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000


# ● СРАВНЕНИЕ СПИСКОВ

# acdc = [1,2,3,4,5,6]
# kiss = [1,2,3,4,5]
# print(acdc > kiss)
# OUTPUT True 
# ●
# acdc = [1,2,3,4,5,6]
# kiss = [1,2,3,4,5,]
# print(acdc == kiss)
# OUTPUT False
# ●
# acdc = [1,2,3,4,5,6,22]
# kiss = [1,2,3,4,5,3,27]
# print(acdc > kiss)

# ● ИЗМЕНЕНИЕ ЭЛЕМЕНТА В СПИСКЕ 

# fire = [27,'torture','uae',3.7,(666,325),['hhd']]
# fire [-1] = {'sugar'}
# print (fire)
# OUTPUT [27, 'torture', 'uae', 3.7, (666, 325), {'sugar'}]


# ●  ПЕРЕБОР ЭЛЕМЕНТОВ В СПИСКЕ 

# mem = ['pochemu tak','Obeme','Ukraine']
# for mem in mem:
#       print (mem)

# ● 
# mem = ['pochemu tak','Obeme','Ukraine']
# for mem in mem:
#       print (f'hello {mem}'a = []
# b = [1,2,3,4]
# c = [1,2,3,[4,5,6]]

# print (len(c))

# OUTPUT 4


# for letter in 'Makers':
#       print(letter)
# OUTPUT
# M
# a
# k
# e
# r
# s

# ● ОЗАГЛАВИТЬ ЭЛЕМЕНТЫ В СПИСКЕ 
# for letter in 'Makers':
#       print(letter.upper())
# OUTPUT
# M
# A
# K
# E
# R
# S


# ● МЕТОДЫ СПИСКОВ

# ● APPEND

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●

# ●


# ● МЕТОД  EXTEND 
# МЕТОД EXTEND ПРИНИМАЕТ СПИСОК 
# И РАСШИРЯЕТ СПИСОК ЗА СЧЕТ ДРУГОГО СПИСКА
# ●
# team = ['Hatfield','Ulrich']
# team2 = ['Mustaine','Newsted']
# team2.extend(team)
# print (team2)

# OUTPUT ['Mustaine', 'Newsted', 'Hatfield', 'Ulrich']

# ●
# team = ['Hatfield','Ulrich']
# team2 = ['Mustaine','Newsted']
# team.extend(team2)
# print (team)

# OUTPUT ['Hatfield', 'Ulrich', 'Mustaine', 'Newsted'


# ● SLICES СРЕЗЫ 

# Срезы позволяют обрезать список, 
# взяв лишь те элементы, которые нужны. 

# lrc = ['new','blood','joins','this earth','and quickly']
# print (lrc[0:4])

# OUTPUT ['new', 'blood', 'joins', 'this earth']

# ● 
# lrc = ['new','blood','joins','this earth','and quickly']
# print (lrc[3:5])

# OUTPUT ['this earth', 'and quickly']

# ●  cgr[::2] # Берем каждый второй элемент

# cgr = ['africa','black devil','hong tashan','wuwuwu','xiongmao',
# 'esse','nanjing','mevius','camel']
# print (cgr[::2])

# OUTPUT  ['africa', 'hong tashan', 'xiongmao', 'nanjing', 'camel']

# ● cgr[2::2] # Начиная со второго элемента берем каждый второй элемент

# cgr = ['africa','black devil','hong tashan','wuwuwu','xiongmao',
# 'esse','nanjing','mevius','camel']
# print (cgr[2::2])
# OUTPUT  ['hong tashan', 'xiongmao', 'nanjing', 'camel']

# ● cgr[4:4:] # Начиная с 4 элемента берем все элементы по 6 элемент

# cgr = ['africa','black devil','hong tashan','wuwuwu','xiongmao',
# 'esse','nanjing','mevius','camel']
# print (cgr[1:5])

# OUTPUT ['black devil', 'hong tashan', 'wuwuwu', 'xiongmao']


# ● cgr[::] # БЕРЕМ ВСЕ ЭЛЕМЕНТЫ

# cgr = ['africa','black devil','hong tashan','wuwuwu','xiongmao',
# 'esse','nanjing','mevius','camel']
# print (cgr[::])

# OUTPUT ['africa', 'black devil', 'hong tashan', 'wuwuwu', 
# 'xiongmao', 'esse', 'nanjing', 'mevius', 'camel'

# ●  cgr [0:-1:2] SLICES START,END, STEP

# cgr = ['africa','black devil','hong tashan','wuwuwu','xiongmao',
# 'esse','nanjing','mevius','camel']
# print (cgr[0:-1:2])

# OUTPUT ['africa', 'hong tashan', 'xiongmao', 'nanjing']

# ● КАК ПОЛУЧИТЬ ЭЛЕМЕНТЫ ВЛОЖЕНННЫХ СПИСКОВ
# names = [
#         ['Tom',11],
#         ['Fred',10],
#         ['Jason',2names = [
#         ['Tom',11],
#         ['Fred',10],
#         ['Jason',25],
#         ['Steve', 3]
# ]
# print (names[3][1])

# # OUTPUT 3 3]
# ]
# print (names[1][0])

# ● КАК ПОЛУЧИТЬ ЭЛЕМЕНТЫ ВЛОЖЕНННЫХ СПИСКОВ

# names = [
#         ['Tom',11],
#         ['Fred',10],
#         ['Jason',25],
#         ['Steve', 3]
# ]
# print (names[3][1])

# # OUTPUT 3


#●  ВОПРОС ОСТАЕТСЯ ОТКРЫТЫМ
# print([digits for digits in range(54,9184) if digits %5==0])

# digits = []
# for i in range(54,9184):
#       if x %5 == 0:
#             digits.append(x)

# print(digits)

# x = []
# for i in range(54,9184):
#       if i %5 ==0:
#             x.append(i)
# print(x)




# ccc = list(range(0,101,5))
# print (ccc)
# OUTPUT [1, 3, 5, 7, 9, 11]

# c = list(range(0,101,5))
# print (c)
# n = list(range(15,155,7))
# print (n)


# 6) Есть список чисел a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. 
# Выведите все элементы, которые меньше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# print ()





# c = ['motorcycles', 'Harley-Davidson','Yamaha']
# print (c)


# ●  deepcopy()
# ВОПРОС ОСТАЕТСЯ ОТКРЫТЫМ 
# import copy
# abcd = ['beer','vodka','tequila']
# abcd2 = copy.deepcopy(abcd)
# abcd2.append ('all alcho drinks')
# print(abcd)
# print(abcd2)


# a = ["Davidson"]
# b = ['Harley']
# b.extend(a)
# print (b)

# ВОПРОС ОСТАЕТСЯ ОТКРЫТЫМ
# suitcase = []
# suitcase.append ('money,clothes,tequila,laptop,charger')
# print (suitcase)

# suitcase.pop([4])
# suitcase.insert(0,'guitar')

# ● HOMEWORK
# suitcase = []
# suitcase.append('money')
# suitcase.append('clothes')
# suitcase.append('tequila')
# suitcase.append('laptop')
# suitcase.append('good mood')
# suitcase.pop(4)
# change = 'guitar'
# suitcase.insert(0,
# print (suitcase)

# ● HOMEWORK
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = list(a)
# a = tuple(a)
# print (a)


# ПРОВЕРКА НА ВХОЖДЕНИЕ 
# IN 

# a = [1,2,3,4]
# print(5 in a)
# OUTPUT False 

# LEN() НАХОЖДЕНИЕ ДЛИНЫ 

# a = []
# b = [1,2,3,4]
# c = [1,2,3,[4,5,6]]

# print (len(c))

# OUTPUT 4




# С ЦИКЛЫ 
# WHILE БЕСКОЕНЧНЫЕ
# FOR КОНЕЧНЫЕ


# while условие:
#       тело цикла 

# count = 0 
# while count < 10:
#       print ('Hello world')
#       print (count)
#       count += 1

# count = 0

# while True:
#       if count >= 10
#       break
#       print('Hello world')
#       count += 1

# ● for - цикл для обхода последовательностей 
# (списки. кортежи. строки.словари. range )


# a = [1,2,3,4,5,6]

# for элемент in  последовательность:
#       тело цикла

# ● ЦИКЛ FOR РАБОТАЕТ ТОЛЬКО ДО ТЕХ ПОР ПОКА В ПОСЛЕДОВАТЕЛЬНОСТИ НЕ ЗАКОНЧАТСЯ ЭЛЕМЕНТЫ 


# a = [1,2,3,4,5,6]
# ● вывести все элементы этого списка 

# a = [1,2,3,4,5,6]

# for i in a:
#       print(i)


# str1 = 'string'
# for py in str1:
#       print(py)

# ● В КОРТЕЖАХ ТОЛЬКО INDEX AND COUNT 

# tuple

# a = ('a','b','c','d')
# Index
# count 

# a = ('a','b','c','d')

# for i in a:
#       print(i)


# ● ВНУТРИ ЦИКЛА МОЖНО ИСПОЛЬЗОВАТЬ ЛЮБЫЕ ОПЕРАЦИИ


# a = [1,2,3,4,5,]
# for i in a:
#       print (i **2)


# a = ['a','b','c','d']
# for i in a:
#       print(i.upper())


# a = [16,24,37,45]
# for i in a:
#       if i % 2 == 0:
#             print (a)



# a = [1,2,3,4,5,6,7,8]
# b = []
# for i in a:
#     if i % 2 ==0:
#         b.append(i)


# ● ДИАПАЗОН ЦЕЛЫХ ЧИСЕЛ 
# ● КОГДА НУЖНО ЗАПУСТИТЬ ЦИКЛ ОПРЕДЕЛНЕООЕ КОЛИЧЕСТВО РАЗ

# for i in range(4):
#       print('Hello Wolrd')


# total = 20
# while True:

# num = input('enter number or stop if you want stop:')

# while num != 'stop':
#       num = int(num)
#       total += num 
#       num = input('enter number or stop if you want stop')



# total = 0
# while True:
#       num = input('enter number or stop if you want stop')
#       if num == 'stop':
#             break
#       total +=int(total)

# ● FROM HOMEWORK

# a = [2,5,8,7,4]
# b = ['четное','нечетное','четное','нечетное']
# for i in a:
#       if i % 2 == 0:
#             b.append ('четное')
# else:
#       b.append('нечетное')
# print(b)



# dict1 = {1:'2',3:'3',4:'4'}
# dict2 = {5:'5',6:'6',7:'7'}

# dict1.update(dict2)

# result = []
# for i in dict1.values():
#       result.append(int(i))

# print(sum(result))





# result = 0
# for i in dict.values 


















