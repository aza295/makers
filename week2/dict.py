# 1) ● СЛОВАРЬ ЭТО ИЗМЕНЯЕМЫЙ НЕУПОРЯДОЧЕННЫЙ ТИП ДАННЫХ, 
# ПРЕДСТАВЛЯЮЩИЙ СОБОЙ НАБОР ЭЛЕМЕНТОВ ПО ТИПУ
# "КЛЮЧ:ЗНАЧЕНИЕ".СЛОВАРИ ЕЩЕ НАЗЫВАЮТ АССОЦИАТИВНЫМИ
# МАССИВАМИ ИЛИ ХЭШ-ТАБЛИЦАМИ


# 2) ● КАК СОЗДАТЬ ПУСТЬЕ СЛОВАРИ 
# dict_ = {}
# dict_1 = dict()
# print(type(dict))
# print(type(dict_1))



# 3) ● ЛИТЕРАЛАМИ СЛОВАРЕЙ ЯВЛЯЮТСЯ {}


# 4) ● МЕТОД ВЫВЕДЕНИЯ ТОЛЬКО КЛЮЧЕЙ ИЗ СЛОВАРЯ

# for i in переменная.keys()

# songs = {'ac dc':'hells bells','kiss':'forever','pantera':'cowboys from hell'}
# for i in songs.keys():
#       print(i)

# OUTPUT:
# ac dc
# kiss
# pantera


# 5) ● МЕТОД ВЫВЕДЕНИЯ ТОЛЬКО ЗНАЧЕНИЙ  ИЗ СЛОВАРЯ

# for i in переменная.values()

# elements = {"Au": "gold", "Fe": "iron", "H": "hydrogen", "O": "oxygen"}
# for i in elements.values():
#       print(i)

# OUTPUT: 
# gold
# iron
# hydrogen
# oxygen

# 6) ● МЕТОД ВЫВЕДЕНИЯ КЛЮЧ - ЗНАЧЕНИЙ  ИЗ СЛОВАРЯ

# clb = {'rhcp':'Kiedis','ratm':'Morello',}
# for i in clb.items():
#       print(clb)

# # OUTPUT 
# {'rhcp': 'Kiedis', 'ratm': 'Morello'}


# 7) ● МЕТОД ВЫВЕДЕНИЯ ОПРЕДЕЛЕННЫХ ЗНАЧЕНИЙ  ИЗ СЛОВАРЯ

# УКАЗЫВАЕМ В СКОБКАХ ПЕРЕМЕННУЮ И В КВАДРАТНЫХ СКОБКАХ КЛЮЧ

#  print(cities['USA'])  


# cities = {'China':'Shanghai','USA':'Seattle','Japan':'Tokyo'}
# print(cities['USA'])

# OUTPUT: Seattle



# 8) ● МЕТОД ИЗМЕНЕНИЯ ОПРЕДЕЛЕННЫХ ЗНАЧЕНИЙ  СЛОВАРЯ

# cities = {'China':'Shanghai','USA':'Seattle','Japan':'Tokyo'}
# cities['USA'] = 'Los-Angeles'
# print(cities)

# OUTPUT: {'China': 'Shanghai', 'USA': 'Los-Angeles', 'Japan': 'Tokyo'}

# 9) ● МЕТОД УДАЛЕНИЯ ОПРЕДЕЛЕННЫХ ЗНАЧЕНИЙ  СЛОВАРЯ

# УКАЗЫВАЕМ DEL, В СКОБКАХ ПЕРЕМЕННУЮ И В КВАДРАТНЫХ СКОБКАХ КЛЮЧ

# lyrics = {'we':'can','build':'it','standing':'strong'}
# del (lyrics['build'])
# print(lyrics)




# 10) ● МЕТОД ПРЕОБРАЗОВАНИЯ СЛОВАРЯ В СПИСОК 

# dictionary = {'a': 1, 'b': 2, 'c': 3} 
# dictionary= list(dictionary) 
# print(dictionary)

#dict_as_list = [('a', 1), ('b', 2), ('c', 3)] 




# 11) ● МЕТОД ПРЕОБРАЗОВАНИЯ СЛОВАРЯ В СПИСОК 

# dictionary = [['a', 1], ['b',2] ,['c', 3]]
# dictionary= dict(dictionary) 
# print(dictionary)

# OUTPUT: {'a': 1, 'b': 2, 'c': 3}






# 12) ●
# d = {a: a ** 2 for a in range(7)}
# print(d)





# 13) ● METHOD GET get(key)
# МЕТОД ВЫВЕДЕНИЯ ТОЛЬКО ЗНАЧЕНИЯ  ИЗ СЛОВАРЯ

# my_dict = {1:'Tom',2:'John',3:'Serj'}
# print(my_dict.get(1))

# OUTPUT: Tom


# В СЛУЧАЕ ЕСЛИ КЛЮЧ ОТСУСТВУЕТ НЕ ВЫДАЕТ ОШИБКУ А ВЫДАЕТ None

# my_dict = {1:'Tom',2:'John',3:'Serj'}
# print(my_dict.get(4))

# OUTPUT None


# my_dict = {1:'Tom',2:'John',3:'Serj'}
# print(my_dict[4])

#  OUTPUT: KeyError: 4

# МЕТОД GET ОЧЕНЬ ЧАСТО ИСПОЛЬЗУЕТСЯ ПРИ РАБОТЕ СО СЛОВАРЯМИ



# 14) ● METHOD CLEAR () 

# foods = {'street':'french fries','home':'soup','street':'hanbaobao'}
# foods.clear()
# print(foods)

# OUTPUT: {}


# 15) ● METHOD COPY () 

# drinks = {'alcho':'vodka','healthy':'water','junk':'coke'}
# drinks2 = drinks.copy()

# drinks ['junk'] = 'red bull'
# print(drinks)
# print(drinks2)


# 16) ● METHOD POP() 

# inf = {'name':'Kate','height':'170','weight':'50'}
# inf.pop('weight')
# print(inf)

# OUTPUT: {'name': 'Kate', 'height': '170'}

# ●  inf = {'name':'Kate','height':'170','weight':'50'}
# deleted = inf.pop('weight')
# print(inf)  #OUTPUT {'name': 'Kate', 'height': '170'}
# print(deleted)  #OUTPUT 50

# ●  В СЛУАЧЕ ЕСЛИ НЕТ ДАННОГО КЛЮЧА ВЫДАЕТ ОШИБКУ 

# inf = {'name':'Kate','height':'170','weight':'50'}
# inf.pop('age')
# print(inf)

# OUTPUT KeyError: 'age'


# 17) ● METHOD  POPITEM()
# POPITEM УДАЛЯЕТ ЛЮБУЮ ПАРУ КЛЮЧ ЗНАЧЕНИЙ НО ПОСЛЕ ВЕРСИИ 3.6 
# УДАЛЯЕТ ПОСЛЕДНИЙ ЭЛЕМЕНТ СЛОВАРЯ 


# phones = {'usa':'apple','china':'xiaomi','korea':'samsung'}
# phones.popitem()
# print(phones)

# OUTPUT: {'usa': 'apple', 'china': 'xiaomi'}

# ● КАК ВЕРНУТЬ УДАЛЕННУЮ ПАРУ КЛЮЧ ЗНАЧЕНИЙ 

# phones = {'usa':'apple','china':'xiaomi','korea':'samsung'}
# deleted = phones.popitem()
# print(phones)
# print (deleted)

# OUTPUT:
# {'usa': 'apple', 'china': 'xiaomi'}
# ('korea', 'samsung')  # УДАЛЕННЫЙ ЭЛЕМЕНТ 



# 18) ● METHOD  SETDEFAULT

# ДАННЫЙ МЕТОД ВОЗВРАЩАЕТ ЗНАЧЕНИЕ КЛЮЧА НО ЕСЛИ ЕГО НЕТ 
# НЕ БРОСАЕТ ИСКЛЮЧЕНИЕ А СОЗДАЕТ КЛЮЧ С КАКИМ ТО ЗНАЧЕНИЕМ 

# 1) dict_ = dict(a=1,b=2,c=3)
# print(dict_.setdefault('c'))

# OUTPUT: 3

# 2) dict_ = dict(a=1,b=2,c=3)
# print(dict_.setdefault('d'))
# OUTPUT None


# 3) dict_ = dict(a=1,b=2,c=3)
# print(dict_.setdefault('d',5))
# print(dict)

# OUTPUT: 5 



# 19) ● METHOD  UPDATE ()
# ДАННЫЙ МЕТОД ОБЪЕДИНЯЕТ ДВА СЛОВАРЯ РАСШИРЯЕТ ОДИН СЛОВАРЬ ЗА СЧЕТ ДРУГОГО

# dc = {1:'Somebody',2:'once',3:'told'}
# dcc = {4:'me',5:'the',6:'world'}
# dc.update(dcc)
# print (dc)

# OUTPUT: {1: 'Somebody', 2: 'once', 3: 'told', 4: 'me', 5: 'the', 6: 'world'}


# ● ЕСЛИ МЫ ХОТИМ ПОЛУЧИТЬ ТОЛЬКО ЗНАЧЕНИЯ БЕЗ КЛЮЧЕЙ

# dc = {1:'Somebody',2:'once',3:'told'}
# dcc = {4:'me',5:'the',6:'world'}
# dc.update(dcc)
# for i in dc.values():
#       print(i)

# OUTPUT:
# Somebody
# once
# told
# me
# the
# world



# 20) ● METHOD  FROMKEYS(SEQ,value)
# seq последовательность 
# value значение 

# ДАННЫЙ МЕТОД СОЗДАЕТ СЛОВАРЬ С КАКИМИ ТО 
# КЛЮЧАМИ ИЗ ПОСЛЕДОВАТЕЛЬНОСТИ 


# numbers = [1,2,3,4,5]
# new_dict = dict.fromkeys(numbers,'and')
# print (new_dict)

# OUTPUT: {1: 'and', 2: 'and', 3: 'and', 4: 'and', 5: 'and'}



#  21) ● ПЕРЕБОР ЭЛЕМЕНТОВ СЛОВАРЕЙ 
# items(), keys(), values ()





#  22) ● METHOD ITEMS



# songs = {'ac dc':'hells bells','kiss':'forever','pantera':'cowboys from hell'}
# for i in songs.keys():
#       print(i)




# #СПОСОБ № 2
# songs = {'ac dc':'hells bells','kiss':'forever','pantera':'cowboys from hell'}
# for i in songs.keys():
#       print(i)

# lyrics = {'On': 'a dark', 'desert': 'highway', 'cool wind': 'in my hair'}
# for i in lyrics.values():
#       print(i)



# lyrics = {'On': 'a dark', 'desert': 'highway', 'cool wind': 'in my hair'}
# lyrics = lyrics.values()
# print(lyrics)






# dict.items() - возвращает пары (ключ, значение).

# dict.keys() - возвращает ключи в словаре.

# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).


# dict.values() - возвращает значения в словаре






# ВОПРОС ОСТАЕТСЯ ОТКРЫТЫМ
# songs.get('kiss')
# songs = {'ac dc':'hells bells','kiss':'forever','pantera':'cowboys from hell'}
# for i in songs.keys():
#       if i == 'kiss':
#             print(i)

# phones = {'usa':'apple','china':'xiaomi','korea':'samsung'}
# deleted = phones.popitem()
# print (deleted)
      
# new_elements = {}

# elements = {"Au": "gold", "Fe": "iron", "H": "hydrogen", "O": "oxygen"}
# for k,v in elements.items():
#       new_elements.setdefault(v,k)
# print(new_elements)



# foods = {'street':'french fries','home':'soup','street':'hanbaobao'}
# foods.clear()
# print(foods





# dicts = {1:'a', 2:'b', 3:'c', 4:'d'}
# new_dicts = {v: k for k,v in dicts.items()}
# print (new_dicts)



# drinks = {'alcho':'vodka','healthy':'water','junk':'coke'}
# drinks2 = drinks.copy()
# print(drinks)
# #









# 9) Создайте словарь с числовыми значениями, пройдитесь циклом по элементам  и замените все чётные числа цифрой 2.
# Пример: Ввод -> a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} Вывод -> a{'a': 1, 'b': 2, 'c': 1, 'd': 5, 'e': 2}


# b= {}
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}

# for i in a:

#       if i %2 == 0:
#             print(i)




# new_elements = {}

# elements = {"Au": "gold", "Fe": "iron", "H": "hydrogen", "O": "oxygen"}
# for k,v in elements.items():
#       new_elements.setdefault(v,k)
# print(new_elements


# dict1 = {1:'2',3:'3',4:'4'}
# dict2 = {5:'5',6:'6',7:'7'}

# dict1.update(dict2)

# result = []
# for i in dict1.values():
#       result.append(int(i))



#  dict_1 = dict()



# phones = {'usa':'apple','china':'xiaomi','korea':'samsung'}
# print (deleted = phones.popitem())





# 10)  Дан словарь, удалите из него все элементы со значениями None. 
# Например: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} -> {'b': 1, 'c': 2, 'e': 3}



# for i in a:
#       if i == None:
#             print(a.remove(None))


# >>> {i:a[i] for i in a if i!=0}
# {1: 'one', 2: 'two', 3: 'three'}


# inf = {'name':'Kate','height':'170','weight':'50'}
# inf.pop('weight')
# print(inf)




# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.

# fruits = {'ananas':'300','peach':'50','orange':'80'}
# print(fruits)
# for k, v in fruits.items:
#       result = []
#       if v % 2 == 0:
#             print(fruits)
      


# dict1 = {1:'2',3:'3',4:'4'}
# dict2 = {5:'5',6:'6',7:'7'}

# dict1.update(dict2)

# result = []
# for i in dict1.values():
#       result.append(int(i))

# print(sum(result))


# 9) Создайте словарь с числовыми значениями, пройдитесь циклом по элементам  и замените все чётные числа цифрой 2. 
# Пример: Ввод -> a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} Вывод -> a{'a': 1, 'b': 2, 'c': 1, 'd': 5, 'e': 2}

# """
# 9) Создать список чисел, пройтись по элементам и вместо четных чисел, поставить строку “четное”, а вместо нечетных “нечетное”,
#  результат записать в новый список и вывести в терминал.
# # """
# my_list = [86, 81, 35, 48, 5, 6]
# new_list = []
# for i in my_list:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print (new_list)





# 8) Создать список чисел, затем пройтись по элементам списка и преобразовать все числа в строку, 
# результат записать в новый список и вывести в терминал.
# """
# # my_list = [1, 2, 3, 4]
# # new_list = []
# # for i in my_list:
# #     new_list.append(str(i))
# # print (new_list)
