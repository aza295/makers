# ● МНОЖЕСТВО (SET) - ЭТО ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ КОТОРЫЙ ПРЕДСТАВЛЯЕТ 
# СОБОЙ НЕУПОРЯДОЧЕННУЮ КОЛЛЕКЦИЮ УНИКАЛЬНЫХ 
# ЭЛЕМЕНТОВ 

# ● МНОЖЕСТВА НЕ ИНДЕКСИРУЮТСЯ, МНОЖЕСТВА НЕ ПОДДЕРЖИВАЮТ 
# ОПЕРАЦИИ СРЕЗОВ ИЛИ ЖЕ ПОЛУЧЕНИЯ 
# ЭЛЕМЕНТОВ ПО ИНДЕКСУ

# ● МНОЖЕСТВА ИЗМЕНЯЕМЫ СЛЕДОВАТЕЛЬНО МОЖНО

# ● ОБЪЕДИНЯТЬ МНОЖЕСТВА 
# ● ДОБАВЛЯТЬ ЭЛЕМЕНТЫ
# ● УДАЛЯТЬ ЭЛЕМЕНТЫ

# ● НЕЛЬЗЯ СОЗДАВАТЬ ПУСТОЕ МНОЖЕСТВО


# ● САМО МНОЖЕСТВО ЯВЛЯЕТСЯ ИЗМЕНЯЕМЫМ И ЕГО МОЖНО МЕНЯТЬ: ОДНАКО 
# ЭЛЕМЕНТЫ МНОЖЕСТВА ЯВЛЯЮТСЯ НЕИЗМЕННЫМИ, ТО ЕСТЬ
# ОТНОСЯТСЯ К НЕИЗМЕНЯЕМЫМ ТИПАМ ДАННЫХ ТАКИХ КАК СТРОКИ ЧИСЛА  

# ● ГДЕ ИСПОЛЬЗУЮТ МНОЖЕСТВА В ТАКИХ СИТУАЦИЯХ
# КОГДА  НУЖНО ПОЛУЧИТЬ ТОЛЬКО УНИКАЛЬНОЕ ЗНАЧЕНИЕ 


# ● ЗАМОРОЖЕННОЕ МНОЖЕСТВО (FROZENSET) НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ
# С ХАРАКТЕРИСТИКАМИ МНОЖЕСТВА

# ● TUPLE -(КОРТЕЖИ) УПОРЯДОЧЕННЫЙ НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ КОТОРЫЙ ПРЕДСТАВЛЯЕТ 
# СОБОЙ ПОСЛЕДОВАТЕЛЬНОСТЬ ЭЛЕМЕНТОВ


# ● ЦИКЛ WHILE




# ● МНОЖЕСТВО 
# empty_set = set()
# empty_dict = {}
# print(type(empty_set))
# print(type(empty_dict))

# OUTPUT
#  <class 'set'>
# <class 'dict'>


# ● CОЗДАНИЕ МНОЖЕСТВА

# a = {'ask',27,30, True, False}
# # print (a)
# b = set('bullet')
# # print(b)
# c = set(range(1,10,2))
# print (c)

# ● МНОЖЕСТВА МОГУТ ХРАНИТЬЬ ТОЛЬКО НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ 
# В КАЧЕСТВЕ ЭЛЕМЕНТОВ

# ms = {'hello',1,False,}
# print (ms)
# OUTPUT {False, 1, 'hello'}

# ● МНОЖЕСТВА НЕ МОГУТ ХРАНИТЬЬ В СЕБЕ ИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ
# ms = {'hello',1,False,[1,2,3]}
# print (ms)
# OUTPUT TypeError: unhashable type: 'list'



# ● СРАВНЕНИЕ МНОЖЕСТВ

# МНОЖЕСТВА МОЖНО СРАВНИВАТЬ РАВНЫЕ МНОЖЕСТВА ЭТО ТАКИЕ МНОЖЕСТВА
# КОТОРЫЕ ХРАНЯТ ОДИНАКОВЫЙ НАБОР ЭЛЕМЕНТОВ 
# ВО МНООЖЕСТВАХ СОДЕРЖАТСЯ ТОЛЬКО УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ 
# ПОРЯДОК РАСПОЛОЖЕНИЯ ЭЛЕМЕНТОВ НЕ ВАЖЕН ГЛАВНОЕ ЕСЛИ ВО МНОЖЕСТВАХ 
# СОДЕРЖАТСЯ ОДИНАКОВЫЕ ЭЛЕМЕНТЫ ТО ТАКИЕ МНОЖЕСТВА ЯВЛЯЮТСЯ РАВНЫМИ

# set1 = {1,5,3,9,8}
# set2 = {9,1,5,3,8}
# print (set1==set2)

# OUTPUT True

# ● ЭТО ПОДТВЕРЖДАЕТ ЧТО ВО МНОЖЕСТВАХ ПОРЯДОК РАСПОЛОЖЕНИЯ 
# # ЭЛЕМЕНТОВ НЕ ВАЖЕН ГЛАВНОЕ ЧТО ИМЕЮТСЯ ОДИНАКОВЫЕ НАБОРЫ 
# ЭЛЕМЕНТОВ 

# set1 = {1,5,3,9,0}
# set2 = {9,1,5,3,8}
# set3 = {1,5,1,3,3,8,8,8,9,9}
# print(set3)
# print (set2==set3)

# # OUTPUT False

# my_set = {1.0,True}
# print (my_set)


# set3 = {1,5,1,3,3,8,8,8,9,9}
# print(len(set3))


# guests = {'tom','jason','james','tom'}
# print(len(guests))
# OUTPUT 3

# ● МЕТОДЫ МНОЖЕСТВ

# 1)● МЕТОД ADD()

# ДОБАВЛЯЕТ ЭЛЕМЕНТ В ЛЮБОЕ МЕСТО ВО МНОЖЕСТВЕ 

# guests = {'Donald','Joe','Barac',}
# guests.add('Sadam')
# print(guests)


# 2) ● МЕТОД UPDATE (),6}
#  ЭТОТ МЕТОД РАСШИРЯЕТ МНОЖЕСТВО ЗА СЧЕТ ДРУГОГО МНОЖЕСТВА

# nums = {1,2,3}
# nums2 = {4,5,6}
# nums.update(nums2)
# print(nums)ere

# nums = {1,2,3}
# nums2 = {4,5,6}
# nums.update({'Here i go again'})ere
# 3) ●  МЕТОД REMOVE ()

# guests = {'Pablo','Escobar','JJ Alen',}
# guests.remove('Escobar')
# print (guests)

# OUTPUT  {'JJ Alen', 'Pablo'}


# 4) ● МЕТОД DISCARD()

# n = {'Swimming','NHL','golf'}
# n.discard('golf')
# print(n)

# OUTPUT {'soccer', 'baseball'}


# 5) ● МЕТОД POP() МЕТОД POP РАНДОМНО УУДАЛЯЕТ КАКОЙ ТО ЭЛЕМЕНТ

# n = {'Swimming','NHL','golf'}
# n.pop()
# print(n)

# 6) ● МЕТОД CLEAR просто очищает множество 

# guests = {'Pablo','Escobar','JJ Alen',}
# guests.clear()
# print (id(guests))


# 7) ● МЕТОД COPY 
# 
# songs = {'unforgiven','powler','iron man'}
# songs2 = songs.copy()
# songs2.add('Holy Wars')
# print (songs)
# print(songs2)



# 8) ● МЕТОД INTERSECTION ()
#  ДАННЫЙ МЕТОД НАХОДИТ ПЕРЕСЕЧЕНИЕ ДВУХ МНОЖЕСТВ 

# music_students = {'John','Slovak','Kidies','Flea'}

# art_students = {'Slovak','Dave','Bruce','Flea',}

# print(music_students.intersection(art_students))

# OUTPUT {'Slovak', 'Flea'}

# ● ДРУГОЙ СПОСОБ ЧУТЬ ПОКОРОЧЕ &

# music_students = {'John','Slovak','Kidies','Flea','Eminem'}

# art_students = {'Slovak','Dave','Bruce','Flea','Eminem'}

# print(music_students & art_students)

# OUTPUT {'Slovak', 'Flea', 'Eminem'}


# 9) ● МЕТОД UNION() 
# ДАННЫЙ МЕТОД ОБЪЕДИНЯЕТ ОБА МНОЖЕСТВА

# music_students = {'John','Slovak','Kidies','Flea','Eminem'}

# art_students = {'Slovak','Dave','Bruce','Flea','Eminem'}

# print(art_students.union(music_students))

# OUTPUT {'Kidies', 'Eminem', 'Slovak', 'Bruce', 'John', 'Flea', 'Dave'}

# ● ДРУГОЙ СПОСОБ ЧУТЬ ПОКОРОЧЕ | SHIFT + 

# music_students = {'John','Slovak','Kidies','Flea','Eminem'}

# art_students = {'Slovak','Dave','Bruce','Flea','Eminem'}

# print(art_students|music_students)

# OUTPUT {'Dave', 'Kidies', 'Slovak', 'Flea', 'Eminem', 'John', 'Bruce'}



# 10) ● МЕТОД   DIFFERENCE
# ВОЗВРАЩАЕТ РАЗНОСТЬ ММНОЖЕСТВ  
# 
# covers = {'zombie','hurt','imagine','paradice city'}
# covers2 = {'drive','back in black','crazy','hurt'}
# print (covers2.difference(covers))

# OUTPUT {'crazy', 'back in black', 'drive'}

# ● ДРУГОЙ СПОСОБ ЧУТЬ ПОКОРОЧЕ - 

# covers = {'zombie','hurt','imagine','paradice city'}
# covers2 = {'drive','back in black','crazy','hurt'}
# print (covers -(covers2))

# OUTPUT {'zombie', 'imagine', 'paradice city'}


# 10) ● МЕТОД  SYMMETRIC _DIFFERENCE ()
# ДАННЫЙ МЕТОД  ВОЗВРАЩЕТ УНИКАЛЬНЫЕ ДЛЯ ОБОИХ МНОЖЕСТВ ЭЛЕМЕНТЫ
# А ПЕРЕСЕКАЮЩИЕСЯ ПРОСТО ОТБРАСЫВАЕТ 

# ВОЗВРАЩАЕТ НЕ ПЕРЕСЕКАЮЩИЕСЯ ДЛЯ ОБОИХ МНОЖЕСТВ ЭЛЕМЕНТЫ

# laptops = {'lenovo', 'Mac', 'Asus','rogue'}
# laptops2 = {'lenovo','rogue','ideapad'}
# print (laptops.symmetric_difference(laptops2))
#  a = 2 2 4 6 

# ВОЗВРАЩАЕТ НАМ TRUE OR FALSE 
# ЛЮБОЙ МЕТОД КОТОРЫЙ НАЧИНАЕТСЯ
# С IS ВСЕГДА ВОЗВРАЩАЕT TRUE OR FALSE 

# ● ЕСЛИ МЕДЖДУ ДВУМЯ МНОЖЕСТВАМИ НЕТ ПЕРЕСЕЧЕНИЯ ВЫВОДИТ TRUE

# ● ЕСЛИ МЕДЖДУ ДВУМЯ МНОЖЕСТВАМИ ЕСТЬ ПЕРЕСЕЧЕНИЯ ВЫВОДИТ FALSE 


# numbers = {1,2,3,4,}
# numbers2 = {7,5,6}
# print(numbers.isdisjoint(numbers2))

# OUTPUT TRUE 

# numbers = {1,2,3,4,}
# numbers2 = {7,1,4}
# print(numbers.isdisjoint(numbers2))

# OUTPUT FALSE 


# 10) ● МЕТОД ISSUPERSET()
# ДАННЫЕ МЕТОДЫ ВОЗВРАЩАЮТ TRUE OR FALSE В ТЕХ СЛУЧАЯХ КОГДА
# МНОЖЕСТВО ЯВЛЯЕТСЯ НАДМНОЖЕСТВОМ

# v = {1,2,3,4,5}
# c = {3,5}
# print(v.issuperset(c))

# OUTPUT TRUE 

# 11) ● МЕТОД ISSUBSET()
#  ДАННЫЕ МЕТОДЫ ВОЗВРАЩАЮТ TRUE OR FALSE  В ТЕХ СЛУЧАЯХ КОГДА
# МНОЖЕСТВО ЯВЛЯЕТСЯ ПОДМНОЖЕСТВОМ

# v = {1,2,3,4,5}
# c = {3,5}
# print(v.issubset(c))
# OUTPUT FALSE



# 12) ● МЕТОД INTERSECTION_UPDATE
# ДАННЫЙ МЕТОД НАХОДИТ ПЕРЕСЕКАЮЩИЕСЯ ЭЛЕМЕНТЫ И ИЗМЕНЯЕТ МНОЖЕСТВО
# ПРИСВАИВАЯ ЕЙ НОВОЕ МНОЖЕСТВО ПЕРЕСЕКАЮЩИХСЯ ЭЛЕМЕНТОВ 



# numbers={1,2,3,4}
# numbers2= {2,5,1}
# numbers.intersection_update(numbers2)
# print (numbers)


# 13) ●  МЕТОД DIFFERENCE_UPDATE

# numbers1 = {1,2,3,4,5}
# numbers2 = {5,2,7,8}
# numbers2.difference_update(numbers1)
# print(numbers2)
# OUTPUT {7 ,8}


# 14) ● МЕТОД SYMMETRIC_DIFFERENCE_UPDATE


# bands = {1,2,3,4,5}
# bands2 = {6,9,0,2,4}
# bands.symmetric_difference_update(bands2)
# print (bands)


# 15) ● ЗАМОРОЖЕННЫЕ МНОЖЕСТВА FROZENSET 
# РЕДКО ИСПОЛЬЗУЮТСЯ 


# my_list = frozenset('makers')
# print(my_list)



# 16) ● КОРТЕЖИ TUPLE

#  можно использовать только два метода 

#  index(value) возвращает индекс первого вхождения элемента 
#  с указанным значением

#  count() количество элементов с указаным значением




# b = 1,2,3,
# # b = #(1,2,3)
# print(b)


# x,y,z = 2, 3
# x# 2
# y# 3
# x, y = (2,3)

#17) ●РАСПАКОВКА UNPACKING 

# str1 = '123'
# dig1,dig2,dig3 = str1
# dig1 #'1'
# dig2 #'2'
# dig3 #'3'
# print (str1)

# list1 = [1,2,3]
# value1,value2,value3 = list1

# tuple1 = (1,2,3)
# val1,val2,val3 = tuple1 


#18) ●ОБМЕН ПЕРЕМЕННЫХ 
 
# x = 10
# y = 20

# x, y = y,x
# x, y =(20,10)

# tuple1 = [1,2,3,4,5,6]
# val1,*val2,val3 = tuple1
# print (tuple1)

# val1, *val2, val3, val4 = tuple1


# 19) ● ЦИКЛ WHILE 

# ПРОЙТИСЬ ЦИКЛОМ И ВЫВЕСТИ ЧИСЛА КРАТНЫЕ 3 
# a = [1,2,3,4,5,6,7,8,9,10]

# index = 0
# while index < len(a):
#       if a[index] %3 ==0:
#             print(a[index])
#       index += 1

# 20) ● ЦИКЛ FOR 

# a = [1,2,3,4,5,6,7,8,9,10]
# for num in a:
#       if num % 3 == 0:
#             print (num)


# a = [1,2,3,4,5,6,7,8,9,10]
# for num in range (1,31):
#       if num % 3 == 0:
#             print (num)


# temperature = 5 

# while temperature < 100:
#       print('ping')
#       temperature += 5

# while True:
#       if temperature <=100


# num = 1 
# while num <= 100:
#       num += 1
#       if num  % 3!=0:
#             print(num)
# while num <= 100:
#       if num % 3 ==0:
#             continue
#       print(num)
      
# НАМНОГО ЛЕГЧЕ ИСПОЛЬЗОВАТЬ RANGE+ FOR 

# for num in range(1,31):
#       if num == 5:
#       if num == 7:
#       if num == 11:
#       if num == 10:
#       if num == 28:

#             continue 
#       print (num)



















