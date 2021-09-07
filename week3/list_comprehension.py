# 1) ● LIST COMPREHENSION IS  ГЕНЕРАТОР СПИСКОВ 
#  ● ВАРИАНТЫ ИСПОЛЬЗОВАНИЙ LIST COMPREHENSION 

# 1. ОБОЙТИ ВСЕ ЭЛЕМЕНТЫ ОПРЕДЕЛЕННОЙ ПОСЛЕДОВАТЕЛЬНОСТИ 
# С КАЖДЫМ ЭЛЕМЕНТОМ СДЕЛАТЬ ДЕЙСТВИЕ И РЕЗУЛЬТАТ ЗАПИСАТЬ В НОВЫЙ СПИСОК 

# 2. ОТФИЛЬТРОВАТЬ ЭЛЕМЕНТЫ ПОСЛЕДОВАТЕЛЬНОСТИ В НОВЫЙ СПИСОК ПО ОПРЕДЕЛЛЕНОМУ УСЛОВИЮ 



# a = [1,2,3,4,5]
# c = [i **2 for i in a ]
# print (c)

# OUTPUT: [1, 4, 9, 16, 25]



# БОЛЕЕ ДОЛГИЙ СПОСОБ 
# a = '10 24 27 987 25'
# b = []
# for i in a.split():
#       b.append(int(i)/5)
# print(b)

# БОЛЕЕ БЫСТРЫЙ

# a = '10 24 27 987 25'
# b = [int(i)/5 for i in a.split()]
# print(b)
# OUTPUT [2.0, 4.8, 5.4, 197.4, 5.0]

# the same result but second one more faster and easier 


# a = ['Mick','Keith','Max','Tim']
#  b =[] 
#  for name in a:
#        b.append(a.capitalize())
#  print (b)

# a = [name.capitalize() for name in a]
# print(a)


# OUTPUT:['Mick', 'Keith', 'Max', 'Tim']


# [действие(элемент)]for элемент in последовательности






# ● 
# b= []
# for num in range(1,100):
#       if num % 13 == 0:
#             b.append(num)
# print(b)

# OUTPUT: [13, 26, 39, 52, 65, 78, 91]


# ● MORE EASIEST WAT TO SOLVE IT 

# b = [i for i in range (1,100)
# if i %13 == 0]
# print(b)

# OUTPUT: [13, 26, 39, 52, 65, 78,]


# a = (1,2,3,4,5,6)
# b  =[]
# for num in a:
#       if num %2 == 0:
#             res = num + 0.5
#             b.append(res)
#       else:
#             res = num +0.6
#             b.append(res)
# print(b)

# OUTPUT: [1.6, 2.5, 3.6, 4.5, 5.6, 6.5]


# ● MORE EASIEST WAT TO SOLVE IT


# a = (1,2,3,4,5,6)
# b = [num +0.5 if num  % 2 == 0 
# else num + 0.6 
# for num in a ]
# print(b)

# OUTPUT: [1.6, 2.5, 3.6, 4.5, 5.6, 6.5]


# b = [12,35,6,3,2,3,5,67,124,45,1,66,12,90]
# res = []
# for num in b:
#       if num % 5 == 0:
#             if num <= 40:
#                   b.append(num *10)
#             else:
#                   b.append(num*6)
# print(res)

# res = [num * 10 if num <= 0 
# else num *6 
# for num in b 
# if num % 5 == 0 ]
# print(res)


# DICT COMPREHENSION

# THIS IS DICT COMPREHENSION:
# a = {'a':1,'b':2}
# b = {value:key for key, value in a.items()}
# print(b)

# OUTPUT: {1: 'a', 2: 'b'}


# 15. Дан словарь, значениями в котором являются другие словари.
#  Замените внутренние словари их значениями. Нужно использовать comprehension.
# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}



# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}









# question 
# a1 = [[1,2,3,4,],[5,6,7],[8,9,10]]
# b = [[num * 5 for inner_list in a1]
#              for num in inner_list]
# print(b)



# a = [[1,2,3,4,],[5,6,7],[8,9,10]]
# c =[[num * 5 for num in inner_list]
#              for inner_list in a]
# print(c)

# question 
# a = {
# 'class1':[87,61,89,76,90,100],
# 'class2':[87,77,98,90],
# 'class3':[90,76,98,99,67]
# }
# b = {}

# for key,value in a.items:
#       b[key]= max(value)
#       print(b)

# ● FIRST WAY 
# a = {
# 'class1':[87,61,89,76,90,100],
# 'class2':[87,77,98,90],
# 'class3':[90,76,98,99,67]
# }
# b = {key:max(value)for key,value in a.items()}
# print(b)

# ● SECOND WAY 
# a = {
# 'class1':[87,61,89,76,90,100],
# 'class2':[87,77,98,90],
# 'class3':[90,76,98,99,67]
# }
# b = {key:mark for key,value in a.items()
#               for mark in value if mark ==
#               max(value)}
# print (b)


# for key, value in a.items():
#       max_mark = value[0]
#       for mark in value[1:]:
#             if mark > max_mark:
#                   max_mark = mark
#       b[key]= max_mark
# print(b)








# a = [[1,2,3,4,],[5,6,7],[8,9,10]]
# b = []
# # res = []
# for inner_list in a:
#       for num in inner_list:
#             b.append(num*5)

# c = []
# for inner_list in a:
#       new_inner_list = []
#       for num in inner_list:
#             new_inner_list.append(num *5)
#       c.append(new_inner_list)
     

# THIS IS ORDINARY METHOD
# a = {'a':1,'b':2}
# b = {}
# for key, item in a.items():
#       b[key]= str (value)

# a = {'a':1,'b':2}

# b = {}
# for key, value in a.items():
#       b[value]= key 









# listone = [2, 3, 4]
# listtwo = [2*i for i in listone if i > 2]
# print(listtwo)
# Вывод:[6, 8]


# list = [4,5,7,9,11,13]
# list2 = [4**i for i in list ]
# print (list2)


# Как это работает:
# В этом примере мы создаём новый список, 
# указав операцию, которую необходимо произвести 
# (2 * i), когда выполняется некоторое условие (if i > 2).
# Обратите внимание, что исходный список при этом не изменяется.
# Преимущество использования генера● торов списков состоит в том, 
# что это заметно сокращает объёмы стандартного кода, 
# необходимого для циклической обработки каждого элемента списка и сохранения его в новом списке.



# x = [i for i in range (1,21)if i %2 == 0]
# print(x)


# list_users = ['Alice','Sam','Ben','James']
# invitations = ['You are invited, ' + name for name in list_users]
# print(invitations)



# list1 = [10,5, -6 ,-8,-12,20,3,14,4]
# list2 = [i for i in list1 if i % 2 == 0 and  i > 0]
# print (list2)



# years = ['1973','1975 year','1965y','1969']
# list_ = [i for i in years if i.isdigit()]
# print(list_


# mems = ['Obeme','Casino','Shrek']
# mems = [len(i)for i in mems]
# print (mems)


# 1) ● IF ELSE STRUCTURE IN LIST COMPREHENSIONS 

# 1) list_ = [i if i %2 != 0 else i ** 2  for i in range (1,11)]
# print (list_)

# 2) list1 = [-5,-12,0,1,2,8,4,5,7]
# list1 = [i if i < 0 else i ** 2 for i in list1 if i %2 == 0]
# print (list1)

# ● ИСПОЛЬЗОВАНИЕ LIST COOMPREHENSION 

# names = ['Tom', 'Peter','Bill', 'Lois21',
# 'Kurt 27','Eddie','Bon','Brian']
# filtered_names = [i + ' Makers' 
# if len(i) >= 5 else i + ' Bootcamp' 
# for i in names if i.isalpha()]
# print(filtered_names)


# OUTPUT: ['Tom Bootcamp', 'Peter Makers', 
# 'Bill Bootcamp', 'Eddie Makers', 
# 'Bon Bootcamp', 'Brian Makers']

# ● ОБЫЧНЫЙ СПОСОБ С ПОМОЩЬЮ ЦИКЛА FOR ДЛИННЫЙ И ДОЛГИЙ ПУТЬ
# filtered_names = []
# for i in names:
#       if i.isalpha():
#             if len(i)>=5:
#                   result = i + 'Makers'
#                   filtered_names.append(result)
#             else:
#           ed_names)
#         result = i + 'Bootcamp'
#                   filtered_names.append(result)
# print(filtered_names)

# , 'PeterMakers', 
# 'BillBootcamp', 'EddieMakers', 
# 'BonBootcamp', 'BrianMakers']
# ● 2)

                                    
# ● 2) C LEN FUNCTION IN LIST COMPRHENSION

# names = ['Tom', 'Peter','Bill', 'Lois21',
# 'Kurt 27','Eddie','Bon','Brian']
# filtered_names = [i + ' Makers' 
# if len(i) >= 5 else i + ' Bootcamp' 
# for i in names if i.isalpha()]
# print(filtered_names)

# OUTPUT:  ['Tom Bootcamp', 'Peter Makers', 'Bill Bootcamp', 'Eddie Makers', 'Bon Bootcamp', 'Brian Makers']


# ● IT'S EXAMPLE FROM HOMEWORK 

# numbers = [1,2,3,4,5,6,7,8,9,10]
# filtered_numbers = [ str(i) + ' True' 
# if i % 2 == 0 
# else  str(i) + ' False' 
# for i in numbers]
# print (filtered_numbers)


# ● WE CAN'T USE ELIF IN LIST COMPREHENSIONS

# ● 2),}
# Raychel = {'name':'Raychel','age':23}
# Robert = {'name': 'Robert','age': 17}

# users = [Raychel,Robert]

# ages = [i.get('age',None) for i in users]
# # print(ages)

# bigger = 0
# smaller = 0
# count = 0

# for x in ages:
#       if x >= 18:
#             bigger += 1
#       else:
#             smaller += 1
#       count += 1

# bigger = bigger * (100/count)
# smaller = smaller * (100/count)

# print(f'percent of users age more than 18: {round(bigger)}percent')
# print(f'percent of users age less than 18: {round(smaller)}percent')




# a = int(input('Введите числа от 1 до 10>'))
# b = {i : i for i in range(1,501) if i % a ==0}
# print (b)(input(' Введите число от 1 до 10'))





# 10. Запросите у пользователя число от 1 до 10. Затем пройдитесь по промежутку чисел от 1 до 500 и запишите в словарь только те числа, которые кратны числу, которое ввел пользователь. Ключом будет само число, а значением его квадрат. Нужно использовать comprehension.
# '''
# x = int(input('Введите число от 1 до 10>'))
# y = {i : i for i in range(1,501)if i % x == 0}
# print(y)(input('Введите число от 1 до 10'))
# '''
# 11. Дан словарь, в котором значениями являются целые числа. Пройдитесь по элементам и замените значения на список чисел от 1 до числа, которое является значением. Нужно использовать comprehension.
# Например: a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} -> {'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}
# '''
# x = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
 
# y = { 
# key: list(range(1, val + 1)) for key, val in x.items() 
# } 
# print(y) 
# '''
# 12. Создайте словарь, где ключами будут строки, а значениями произвольные числа. Затем пройдитесь по элементам и запишите вместо значения строку 'even', если значение четное, а если нет то 'odd'. Нужно использовать comprehension.
# '''

# z = {'a': 2, 'b': 7, 'c': 3, 'd': 8, 'e': 4} 
 
# v = { 
#   key: 'odd' if value % 2 != 0 
#   else 'even' 
#   for key, value in z.items() 
# } 
# print(v)

# '''
# 13. Дано предложение 'In 1984 there were 13 instances of a protest with over 1000 people attending'. Получите список чисел из этого предложения. Нужно использовать comprehension.
# '''
# list_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'.split() 
 
# new_list = [int(i) for i in list_ if i.isdigit()] 
# print(new_list)

# '''
# 14. Дан словарь, в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам. Замените оценки названием предмета, по которому студент имеет высший балл. Нужно использовать comprehension.
# Например: a = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
#                'Olga': {'history': 92, 'math': 96, 'literature': 81},
#                'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# Результат: {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}
# '''

# a = { 
#   'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
#   'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
#   'Nik': {'history': 84, 'math': 85, 'literature': 87} 
#   } 
 
# b = { 
#   key: inner_key for key, val in a.items() 
#                  for inner_key, inner_val in val.items() if inner_val == max(inner_val for inner_val in val.values()) 
# } 
# print(b)
# '''
# 15. Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Нужно использовать comprehension.
# Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
# '''
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
 
# new_dict = { 
#   key: inner_val for key, val in my_dict.items() 
#                  for inner_key, inner_val in val.items() 
# } 
# print(new_dict)

































# numbers = [1,2,3,4,5,6,7,8,9,10]
# filtered_numbers = [ str(i) + ' True' 
# if i % 2 == 0 
# else  str(i) + ' False' 
# for i in numbers]
# print (filtered_numbers)











