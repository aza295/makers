# Область видимости переменных в функциях

# У ПЕРЕМЕННЫХ ЕСТЬ ТАКОЕ ВАЖНОЕ СВОЙСТВО КАК ОБЛАСТЬ ВИДИМОСТИ  

#Example №1 

# ● 1) РАБОТА С ЛОКАЛЬНЫМИ ПЕРЕМЕННЫМИ


# ● ЛОКАЛЬНЫЕ ПЕРЕМЕННЫЕ ЭТО ПЕРЕМЕННЫЕ,ОБЪЯВЛЕННЫЕ ВНУТРИ ЛЮБОГО БЛОКА ПРОГРАММЫ  
# И ДОСТУПНЫЕ ТОЛЬКО В ПРЕДЕЛАХ ЭТОГО КОДА,БЛОКА

# def f(a,b):
#       a = 45 # НА ДАННЫЙ МОМЕНТ  a является локальной переменной 
#       b = 5  # НА ДАННЫЙ МОМЕНТ  b является локальной переменной 
#       print(a)
#       print(b)
# print(a)
# print(b)

# OUTPUT: NameError: name 'a' is not defined 

# #ЭТА ОШИБКА ВЫВОДИТСЯ ПОТОМУ ЧТО a,b ЯВЛЯЮТСЯ ЛОКАЛЬНЫМИ ПЕРЕМЕННЫМИ
# ЭТО ЗНАЧИТ ЧТО ИХ БУДЕТ ВИДНО ТОЛЬКО ВНУТРИ ФУНКЦИИ 
# PYTHON ИХ НЕ РАСПОЗНАЕТ ПОТОМУ ЧТО ОНИ БЫЛИ ТОЛЬКО ВНУТРИ ФУНКЦИИ 
# ИХ ОБЛАСТЬ ВИДИМОСТИ ТОЛЬКО ВНУТРИ ЭТОЙ ФУНКЦИИ Example №1


# ● 2) РАБОТА С ГЛОБАЛЬНЫМИ ПЕРЕМЕННЫМИ

# ● ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ - ЭТО ПЕРЕМЕННАЯ ДОСТУПНАЯ В ЛЮБОМ МЕСТЕ ПРОГРАММЫ 

# a = 45  # НА ДАННЫЙ МОМЕНТ a ЯВЛЯЕТСЯ  ГЛОБАЛЬНОЙ ПЕРЕМЕННОЙ 
# b = 5   # НА ДАННЫЙ МОМЕНТ b ЯВЛЯЕТСЯ  ГЛОБАЛЬНОЙ ПЕРЕМЕННОЙ 
# def f(a,b):
#       a = 45  
#       b = 5

# print(a)
# print(b)

# OUTPUT: 45,5

# В ДАННОМ ПРИМЕРЕ НЕ ВЫХОДИТ ОШИБКА ТАК КАК МЫ ЗАДАЛИ ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ
# PYTHON ВИДИТ ИХ И ВЫВОДИТ 


# ● 3) РАБОТА С ОПЕРАТОРОМ global

# В СЛУЧАЕ ЕСЛИ У НАС ЕСТЬ ПЕРЕМЕННАЯ КОТОРАЯ ЯВЛЯЕТСЯ ГЛОБАЛЬНОЙ,
# НО МЫ ХОТИМ ИСПОЛЬЗОВАТЬ И МЕНЯТЬ ЕЕ ВНУТРИ ФУНКЦИЙ.
# ДЛЯ ЭТОГО ЕСТЬ СПЕЦИАЛЬНЫЙ ОПЕРАТОР КОТОРЫЙ НАЗЫВАЕТСЯ  global

# ЧТО МЫ СОБИРАЕМСЯ ДЕЛАТЬ МЫ ХОТИМ ИСПОЛЬЗОВАТЬ ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ a
# ВНУТРИ ФУНКЦИИ ПРИ ЭТОМ НЕ ИЗМЕНЯЯ ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ 
# ДЛЯ ЭТОГО НАМ НЕОБХОДИМО ИСПОЛЬЗОВАТЬ global


# x = 3
# z = 7
# def f():
#       global x
#       x = x +2
#       return x
# f() 
# print(x)

# OUTPUT: 5
#ЗНАЧИТ ФУНКЦИЯ ЗАРАБОТАЛА 

# ЧТО ПРОИЗОШЛО: ПРИ ПОМОЩИ ОПЕРАТОРА global МЫ ВЗЯЛИ ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ a
# ИЗМЕНИЛИ ЕЕ ВНУТРИ ФУНКЦИИ И ВЫВЕЛИ ЕЕ УЖЕ ИЗМЕНЕННУЮ 


# print(x) # ---- 3  В ДАННОМ ПРИМЕРЕ  РЕЗУЛЬТАТ РАВЕН 3 ТАК КАК МЫ ВЫЗЫВАЕМ ЕЕ 
# ДО ФУНКЦИИ И НАША global НЕ  ОТРАБОТАЕТ
# f() # УЖЕ ВЫЗВАЛИ ФУНКЦИЮ
# print(x) # ---- 5 В ДАННОМ ПРИМЕРЕ  РЕЗУЛЬТАТ РАВЕН 5 ТАК КАК МЫ ВЫЗЫВАЕМ ЕЕ 
# ПОСЛЕ ФУНКЦИИ И НАША global УЖЕ ОТРАБОТАЛА





# ● 4) BUILT-INS ЭТО ВСТРОЕННОЕ ПРОСТРАНОСТВО ИМЕН 
# ЧТОБЫ УЗНАТЬ КАКИЕ ОБЪЕКТЫ ЯВЛЯЮТСЯ ВСТРОЕННЫМИ В python МЫ ИСПОЛЬЗУЕМ
# __builtins__


# print(dir(__builtins__))
# OUTPUT: ВЫВОДИТ ПЕРЕЧЕНЬ ОБЪЕКТОВ КОТОРЫЕ ЯВЛЯЮТСЯ ВСТРРОЕННЫМИ В python




# ● 4 ГЛОБАЛЬНОЕ ПРОСТРАНСТВО ИМЕН 


# name = 'makers'
# name = 'bootcamp'
# print(name)

# OUTPUT: bootcamp потому что  python ПЕРЕЗАПИСЫВАЕТ НАШУ ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ
# НА НОВОЕ ЗНАЧЕНИЕ ТАК КАК name = 'bootcamp ' ОН БЫЛ ОБЪЯВЛЕН ПОЗЖЕ,
# И ПОЭТОМУ python ПЕРЕЗАПИСАЛ ЕГО,ТЕПЕРЬ python НЕ ХРАНИТ В СЕБЕ В ПЕРЕМЕННОЙ
# name ЗНАЧЕНИЕ makers. ПРОИЗОШЛО ПЕРЕНАПРАВЛЕНИЕ 



# ● 4 ЛОКАЛЬНОЕ ПРОСТРАНСТВО ИМЕН 

# words = "for me to say"

# def func_a():
#       words = "how can i find a way"
#       print(words)

# func_a() #OUTPUT: "how can i find a way"
# print(words) #OUTPUT: "for me to say"


# ● 5 ЗАМКНУТОЕ ПРОСТРАНСТВО ИМЕН


# lyrics = 'welcome to where'
# def outer():  #ВНУТРИ ЭТОЙ ФУНКЦИИ СОЗДАЕМ ПЕРЕМЕННУЮ LYRICS
#       lyrics = 'time stands'
#       print(lyrics)

#       def inner():  #ВНУТРИ НАРУЖНЕЙ ФУНКЦИИ DEF OUTER МЫ СОЗДАЕМ ЕЩЕ ОДНУ ФУНКЦИЮ
#             lyrics = 'still, no one leaves' #ВНУТРИ ЭТОЙ ФУНКЦИИ ТОЖЕ СОЗДАЕМ ПЕРЕМЕННУЮ LYRICS
#             print(lyrics)

#       inner() # НАМ НЕОБХОДИМО ЧТОБЫ ФУНКЦИЯ OUTER  ВНУТРИ СЕБЯ ВЫЗЫВАЛА INNER ПОЭТОМУ НАМ НЕОБХОДИМО 
# outer()
# print(lyrics)



# 2. Пользователь должен ввести 2 целых числа,
#  Вам необходимо проверить делится ли первое число на второе. 
#  Вывести результат, а также остаток от деления (если есть)


# a = (45,27,5)
# print(max(a)


# 6. Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
# Но в ночной клуб пропускают только тех, кому 17+.
# Мурату - 24 года, Эржану - 21 год, Чынгызу - 24 года, Алтынай - 17 лет, Асеме - 16.
# Напишите программу которая определяет кого пустить в ночной клуб, а кого нет.
# """


# Т = int[24]
# Эржан - 21 




# 5. Вам дан список из целых чисел. Напишите функцию для вычисления
#  факториала каждого из чисел, результат записать в новый список.





# 5. Вам дан список из целых чисел.
#  Напишите функцию для вычисления факториала каждого из чисел,
#   результат записать в новый список.

# def count_characters (string):
#     vowels_count = 0
#     consonants_count = 0
#     others_count = 0
#     vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
#     for chr in string.lower():
#         if chr in vowels:
#             vowels_count += 1
#         elif chr.isalpha():
#             consonants_count += 1
#         else:
#             others_count += 1
#     print (f'Количество гласных: {vowels_count}')
#     print (f'Количество согласных: {consonants_count}')
#     print (f'Количество остальных символов: {others_count}')
 


# 7. Вам дан список из нескольких имён в нижнем регистре. 
# Напишите функцию которая записывает первую букву имени в верхнем регистре и сохраняет результат в новом списке.
# """
# 10. Вам дан список целых чисел. Напишите программу
# которая выводит все элементы, которые меньше 7.


# list = ['dave','tom','scott','james'] #  В НАЧАЛЕ МЫ СОЗДАЕМ СПИСОК С ИМЕНАМИ 
# list2 =[] #ДАЛЕЕ СОЗДАЕМ ПУСТОЙ СПИСОК КУДА БУДЕМ ВКЛАДЫВАТЬ ЗНАЧЕНИЯ  ПЕВРОГО СПИСКА С ИМЕНАМИ 
# for list in list: #ОБРАЩАЕМСЯ К НАШЕМУ СПИСКУ С ИМЕНАМИ 
#     list2.append(list.title()) # В ПУСТОЙ СПИСОК ДОБАВЛЯЕМ ЗНАЧЕНИЯ LIST С ПОМОЩИ APPEND  И ПЕРЕВОДИМ В ВЕРХНИЙ РЕГИСТР ПРИ ПОМОЩИ TITLE
# print(list2)

# 10. Вам дан список целых чисел. Напишите программу
# которая выводит все элементы, которые меньше 7.

a = 27
b = 3
c = 19
z = a,b,c
for z in z:
    if z < 7:
        print(z)
    else:
        print()
        





















# Область видимости указывает интерпретатору, 
# когда наименование (или переменная) видимо.
# Другими словами, область видимости определяет, 
# когда и где вы можете использовать свои переменные, 
# функции, и т.д. Если вы попытаетесь использовать что-либо,
# что не является в вашей области видимости, вы получите ошибку NameError.


# Python содержит четыре разных типа области видимости

# Локальная область видимости (local)
# Нелокальная область видимости (non local,enclosed)
# Встроенная (built-in)
# Глобальная область видимости (global)








































































































